# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

import hashlib
import time
from lxml import etree

from receive_message import BasicReceive
from receive_event import BasicEvent
from send_message import BasicSend, SendText
from image_how_old import image_how_old


WECHAT_TOKEN = "canux"


@csrf_exempt
def wechat_varify(request):
    """Basic function used to conmunicate with wechat.

    GET means wechat server make connection with django server.
    POST means wechat user send message to wechat server and transfer to django server,
    And django server send message back to wechat server and transfer to wechat user.
    """
    if request.method == "GET":
        # Wechat server sent GET request to the URL to verify.
        return HttpResponse(WechatRequest.get_request(request))
    elif request.method == "POST":
        # Wechat user POST the message to the URL with XML format.
        return HttpResponse(WechatRequest.post_request(request))
    else:
        return None


class WechatRequest(object):

    """Implement the basic function for GET and POST.

    request is django.http.HttpRequest object.
    """

    @staticmethod
    def get_request(request):
        token = WECHAT_TOKEN
        timestamp = request.GET.get("timestamp", None)
        nonce = request.GET.get("nonce", None)
        signature = request.GET.get("signature", None)
        echostr = request.GET.get("echostr", None)

        tmp_list = [token, timestamp, nonce]
        tmp_list.sort()
        tmp_str = "%s%s%s" % tuple(tmp_list)
        tmp_str = hashlib.sha1(tmp_str).hexdigest()

        if tmp_str == signature:
            return echostr
        else:
            return None

    @staticmethod
    def post_request(request):
        request_map = MessageUtil.parse_xml(request)
        # All receive messages have this arguments.
        to_user_name = request_map.get(u'ToUserName')
        from_user_name = request_map.get(u'FromUserName')
        create_time = request_map.get(u'CreateTime')
        msg_type = request_map.get(u'MsgType')
        msg_id = request_map.get(u'MsgId')

        # Init basic arguments for SendText object.
        send_text_object = SendText()
        send_text_object.set_to_user_name(from_user_name)
        send_text_object.set_from_user_name(to_user_name)
        send_text_object.set_create_time(time.time())
        send_text_object.set_msg_type(BasicSend.RESP_MESSAGE_TYPE_TEXT)

        # Response to different request message type.
        if msg_type == BasicReceive.REQ_MESSAGE_TYPE_TEXT:
            # Receive text message from wechat user.
            receive_text_content = request_map.get(u'Content')
            send_text_content = receive_text_content
        elif msg_type == BasicReceive.REQ_MESSAGE_TYPE_IMAGE:
            # Get image message from wechat user.
            pic_url = request_map.get('PicUrl')
            send_text_content = image_how_old(pic_url)
        elif msg_type == BasicReceive.REQ_MESSAGE_TYPE_VOICE:
            pass
        elif msg_type == BasicReceive.REQ_MESSAGE_TYPE_VIDEO:
            pass
        elif msg_type == BasicReceive.REQ_MESSAGE_TYPE_LOCATION:
            pass
        elif msg_type == BasicReceive.REQ_MESSAGE_TYPE_LINK:
            pass
        elif msg_type == BasicReceive.REQ_MESSAGE_TYPE_EVENT:
            event_type = request_map.get(u'Event')
            if event_type == BasicEvent.EVENT_TYPE_SUBSCRIBE:
                send_text_content = "感谢您的关注!"
            elif event_type == BasicEvent.EVENT_TYPE_UNSUBSCRIBE:
                pass
            elif event_type == BasicEvent.EVENT_TYPE_LOCATION:
                pass
            elif event_type == BasicEvent.EVENT_TYPE_CLICK:
                pass
            elif event_type == BasicEvent.EVENT_TYPE_VIEW:
                pass
            elif event_type == BasicEvent.EVENT_TYPE_SCANCODE_WAITMSG:
                pass
            elif event_type == BasicEvent.EVENT_TYPE_SCANCODE_PUSH:
                pass
            else:
                send_text_content = '输入无法识别的事件类型。'
        else:
            send_text_content = '输入无法识别的消息类型。'

        send_text_object.set_content(send_text_content)
        # Transfer message to xml format.
        send_xml = MessageUtil.to_xml(send_text_object)
        # Send the xml to wechat user.
        return send_xml


class MessageUtil(object):

    """Tools to transfer xml and string format messages.

    Wechat server POST the xml format message to django server,
    And django server need to POST xml format message to wechat server too.
    Define the message type, and get the message with xml format and parser it.
    """

    @staticmethod
    def parse_xml(request):
        """Parse receive message with xml format from wechat server."""
        str_xml = request.body.decode(u'utf-8')
        req_xml = etree.fromstring(str_xml)
        dict_xml = {}
        for node0 in req_xml:
            dict_tmp0 = {}
            for node1 in node0.getchildren():
                dict_tmp0[node1.tag] = node1.text
            if any(dict_tmp0):
                dict_xml[node0.tag] = dict_tmp0
            else:
                dict_xml[node0.tag] = node0.text
        return dict_xml

    @staticmethod
    def to_xml(message_object):
        """Convert send message object to xml format and send to wechat server."""
        root = etree.Element(u'xml')
        for key, value in vars(message_object).items():
            if key in BasicSend.MESSAGETYPE:
                tmproot = etree.SubElement(root, key)
                if key == u'News':
                    for each_news in value:
                        etree.SubElement(tmproot, u'item')
                        for tmpkey, tmpvalue in vars(each_news).items():
                            tmpkey_ele = etree.SubElement(tmproot, tmpkey)
                            tmpkey_ele.text = etree.CDATA(unicode(tmpvalue))
                else:
                    for tmpkey, tmpvalue in vars(message_object.__getattribute__(key)).items():
                        tmpkey_ele = etree.SubElement(tmproot, tmpkey)
                    if u'time' in tmpkey.lower() or u'count' in tmpkey.lower():
                        tmpkey_ele.text = unicode(tmpvalue)
                    else:
                        tmpkey_ele.text = etree.CDATA(unicode(tmpvalue))
            else:
                if u'time' in key.lower() or u'count' in key.lower():
                    etree.SubElement(root, key).text = unicode(value)
                else:
                    etree.SubElement(root, key).text = etree.CDATA(unicode(value))
        return etree.tostring(root, pretty_print=True, xml_declaration=False, encoding=u'utf-8')
