# -*- coding: utf-8 -*-
# from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

import hashlib

# TPL
from lxml import etree

from receive_message import BasicReceive, TextMsg, ImageMsg
from send_message import BasicSend, Text
from image_how_old import image_how_old

WECHAT_TOKEN = u"canux"

# Send/response message types to wechat user.
RESP_MESSAGE_TYPE_TEXT = u'text'
RESP_MESSAGE_TYPE_IMAGE = u'image'
RESP_MESSAGE_TYPE_VOICE = u'voice'
RESP_MESSAGE_TYPE_VIDEO = u'video'
RESP_MESSAGE_TYPE_MUSIC = u'music'
RESP_MESSAGE_TYPE_NEWS = u'news'
MESSAGE_TYPE = [u'text', u'image', u'voice', u'video', u'music', u'news']

# Receive/request message type from wechat user.
REQ_MESSAGE_TYPE_TEXT = u'text'
REQ_MESSAGE_TYPE_IMAGE = u'image'
REQ_MESSAGE_TYPE_VOICE = u'voice'
REQ_MESSAGE_TYPE_VIDEO = u'video'
REQ_MESSAGE_TYPE_SHORTVIDEO = u'shortvideo'
REQ_MESSAGE_TYPE_LOCATION = u'location'
REQ_MESSAGE_TYPE_LINK = u'link'
REQ_MESSAGE_TYPE_EVENT = u'event'

# Event type from wechat user.
Event_SUBSCRIBE = u'subscribe'
Event_UNSUBSCRIBE = u'unsubscribe'
Event_SCAN = u'SCAN'
Event_LOCATION = u'LOCATION'
Event_CLICK = u'CLICK'
Event_VIEW = u'VIEW'


@csrf_exempt
def wechat_varify(request):
    """Basic function used to conmunicate with wechat.

    GET means wechat server make connection with django server.
    POST means wechat user send message to wechat server and transfer to django server,
    And django server send message back to wechat server and transfer to wechat user.
    """
    if request.method == "GET":
        # Wechat server sent GET request to the URL to verify.
        print("Start to get")
        return HttpResponse(WechatRequest.get_request(request))
    elif request.method == "POST":
        # Wechat user POST the message to the URL with XML format.
        print("Start to post")
        return HttpResponse(WechatRequest.post_request(request))
    else:
        return None


class WechatRequest(object):

    """Implement the basic function for GET and POST.

    request is django.http.HttpRequest object.
    response is django.http.HttpResponse object.
    """

    @staticmethod
    def get_request(request):
        signature = request.GET.get("signature", None)
        timestamp = request.GET.get("timestamp", None)
        nonce = request.GET.get("nonce", None)
        echostr = request.GET.get("echostr", None)
        token = WECHAT_TOKEN

        tmp_list = [token, timestamp, nonce]
        tmp_list.sort()

        # Wechat office method
        sha1 = hashlib.sha1()
        map(sha1.update, tmp_list)
        hashcode = sha1.hexdigest()

        # My own method
        # tmp_str = '%s%s%s' % tuple(tmp_list)
        # hashcode = hashlib.sha1(tmp_str).hexdigest()

        if hashcode == signature:
            print("get succeed")
            return echostr
        else:
            print("get failed")
            return ""

    @staticmethod
    def post_request(request):
        request_map = MessageUtil.parse_xml(request)
        print(request_map)
        receive_basic_object = BasicReceive(request_map)
        MsgType = receive_basic_object.MsgType
        print(MsgType)
        ToUserName = receive_basic_object.ToUserName
        print(ToUserName)
        FromUserName = receive_basic_object.FromUserName
        print(FromUserName)

        # Response to different request message type.
        if MsgType == REQ_MESSAGE_TYPE_TEXT:
            receive_text_object = TextMsg(request_map)
            Content = receive_text_object.Content
            send_text_object = Text(FromUserName, ToUserName, Content)
            return send_text_object.send()
        elif MsgType == REQ_MESSAGE_TYPE_IMAGE:
            receive_image_object = ImageMsg(request_map)
            PicUrl = receive_image_object.PicUrl
            Content = image_how_old(PicUrl)
            send_text_object = Text(FromUserName, ToUserName, Content)
            return send_text_object.send()
        elif MsgType == REQ_MESSAGE_TYPE_VOICE:
            return BasicSend().send()
        elif MsgType == REQ_MESSAGE_TYPE_VIDEO:
            return BasicSend().send()
        elif MsgType == REQ_MESSAGE_TYPE_SHORTVIDEO:
            return BasicSend().send()
        elif MsgType == REQ_MESSAGE_TYPE_LOCATION:
            return BasicSend().send()
        elif MsgType == REQ_MESSAGE_TYPE_LINK:
            return BasicSend().send()
        elif MsgType == REQ_MESSAGE_TYPE_EVENT:
            Event = request_map.get(u'Event')
            if Event == Event_SUBSCRIBE:
                return BasicSend().send()
            elif Event == Event_UNSUBSCRIBE:
                return BasicSend().send()
            elif Event == Event_SCAN:
                return BasicSend().send()
            elif Event == Event_LOCATION:
                return BasicSend().send()
            elif Event == Event_CLICK:
                return BasicSend().send()
            elif Event == Event_VIEW:
                return BasicSend().send()
            else:
                return BasicSend().send()
        else:
            return BasicSend().send()


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
