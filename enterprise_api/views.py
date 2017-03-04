# -*- coding: utf-8 -*-
# from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.conf import settings

# TPL
from lxml import etree

from utils.WXBizMsgCrypt import WXBizMsgCrypt
from receive_message import BasicReceive, TextMsg, ImageMsg
from response_message import BasicResponse, Text
from how_old import handle_how_old
from tuling_robot import handle_tuling_robot

# Receive message type from wechat user.
REC_MESSAGE_TYPE_TEXT = u'text'
REC_MESSAGE_TYPE_IMAGE = u'image'
REC_MESSAGE_TYPE_VOICE = u'voice'
REC_MESSAGE_TYPE_VIDEO = u'video'
REC_MESSAGE_TYPE_SHORTVIDEO = u'shortvideo'
REC_MESSAGE_TYPE_LOCATION = u'location'
REC_MESSAGE_TYPE_LINK = u'link'
REC_MESSAGE_TYPE_EVENT = u'event'

# Event type from wechat user.
EVENT_SUBSCRIBE = u'subscribe'
EVENT_UNSUBSCRIBE = u'unsubscribe'
EVENT_LOCATION = u'LOCATION'
EVENT_CLICK = u'CLICK'
EVENT_VIEW = u'VIEW'
EVENT_SCANCODE_PUSH = u'scancode_push'
EVENT_SCANCODE_WAITMSG = u'scancode_waitmsg'
EVENT_PIC_SYSPHOTO = u'pic_sysphoto'
EVENT_PIC_PHOTO_OR_ALBUM = u'pic_photo_or_album'
EVENT_PIC_WEIXIN = u'pic_weixin'
EVENT_LOCATION_SELECT = u'location_select'
EVENT_ENTER_AGENT = u'enter_agent'
EVENT_BATCH_JOB_RESULT = u'batch_job_result'

# Response message types to wechat user.
RESP_MESSAGE_TYPE_TEXT = u'text'
RESP_MESSAGE_TYPE_IMAGE = u'image'
RESP_MESSAGE_TYPE_VOICE = u'voice'
RESP_MESSAGE_TYPE_VIDEO = u'video'
RESP_MESSAGE_TYPE_NEWS = u'news'
MESSAGE_TYPE = [u'text', u'image', u'voice', u'video', u'news']

# 企业号的ID.
CORPID = settings.CORPID
# Token可由企业任意填写，用于生成签名。
TOKEN = settings.TOKEN
# EncodingAESKey用于消息体的加密，是AES密钥的Base64编码。
EncodingAESKey = settings.ENCODINGAESKEY


@csrf_exempt
def wechat_varify(request):
    """Basic function used to communicate with wechat.

    GET means wechat server make connection with django server.
    POST means wechat user send message to wechat server and transfer to django server,
    And django server send message back to wechat server and transfer to wechat user.
    """
    if request.method == "GET":
        # Wechat server sent GET request to the URL to verify.
        return HttpResponse(WechatRequest.get_request(request), content_type="text/plain")
    elif request.method == "POST":
        # Wechat user POST the message to the URL with XML format.
        return HttpResponse(WechatRequest.post_request(request), content_type="application/xml")
    else:
        return None


class WechatRequest(object):

    """Implement the basic function for GET and POST.

    request is django.http.HttpRequest object.
    response is django.http.HttpResponse object.
    """

    @staticmethod
    def get_request(request):
        """开启回调模式，微信服务器会发送http-GET给企业的URL并验证．

        企业号将发送GET请求到填写的URL上，GET请求携带四个参数，企业在获取时需要做urldecode处理.
        企业通过参数msg_signature对请求进行校验，如果确认此次GET请求来自企业号，那么企业应该对echostr参数解密并原样返回echostr明文.
        (不能加引号，不能带bom头，不能带换行符)，则接入验证生效，回调模式才能开启。
        """
        wxbmc = WXBizMsgCrypt(TOKEN, EncodingAESKey, CORPID)
        msg_signature = request.GET.get('msg_signature')
        timestamp = request.GET.get('timestamp')
        nonce = request.GET.get('nonce')
        # echostr首次校验时必带
        echostr = request.GET.get('echostr')
        ret, reply_echostr = wxbmc.VerifyURL(msg_signature, timestamp, nonce, echostr)
        if ret != 0:
            return ret
        return reply_echostr

    @staticmethod
    def post_request(request):
        """使用回调模式，用户通过微信企业号给企业的URL通过http-POST发送消息，企业对此进行回复．

        企业号在回调企业URL时，会对消息体本身做AES加密，以XML格式POST到企业应用的URL上；
        企业在被动响应时，也需要对数据加密，以XML格式返回给微信。
        """
        wxbmc = WXBizMsgCrypt(TOKEN, EncodingAESKey, CORPID)
        postdata = request.body
        msg_signature = request.GET.get('msg_signature')
        timestamp = request.GET.get('timestamp')
        nonce = request.GET.get('nonce')
        ret, xml_content = wxbmc.DecryptMsg(postdata, msg_signature, timestamp, nonce)
        if ret != 0:
            return ret
        request_map = MessageUtil.parse_xml(xml_content)
        receive_basic_object = BasicReceive(request_map)
        MsgType = receive_basic_object.MsgType
        ToUserName = receive_basic_object.ToUserName
        FromUserName = receive_basic_object.FromUserName

        # Response to different request message type.
        if MsgType == REC_MESSAGE_TYPE_TEXT:
            receive_text_object = TextMsg(request_map)
            receive_content = receive_text_object.Content
            response_content = handle_tuling_robot(receive_content, FromUserName)
            if not response_content:
                response_content = u"Useless text!"
            response_text_object = Text(FromUserName, ToUserName, response_content)
            ret, encryptmsg = wxbmc.EncryptMsg(response_text_object.response(), nonce, timestamp)
            if ret != 0:
                return BasicResponse().response()
            return encryptmsg
        elif MsgType == REC_MESSAGE_TYPE_IMAGE:
            receive_image_object = ImageMsg(request_map)
            PicUrl = receive_image_object.PicUrl
            response_content = handle_how_old(PicUrl)
            if not response_content:
                response_content = u"Useless image!"
            response_image_object = Text(FromUserName, ToUserName, response_content)
            ret, encryptmsg = wxbmc.EncryptMsg(response_image_object.response(), nonce, timestamp)
            if ret != 0:
                return BasicResponse().response()
            return encryptmsg
        elif MsgType == REC_MESSAGE_TYPE_VOICE:
            return BasicResponse().response()
        elif MsgType == REC_MESSAGE_TYPE_VIDEO:
            return BasicResponse().response()
        elif MsgType == REC_MESSAGE_TYPE_SHORTVIDEO:
            return BasicResponse().response()
        elif MsgType == REC_MESSAGE_TYPE_LOCATION:
            return BasicResponse().response()
        elif MsgType == REC_MESSAGE_TYPE_LINK:
            return BasicResponse().response()
        elif MsgType == REC_MESSAGE_TYPE_EVENT:
            Event = request_map.get(u'Event')
            if Event == EVENT_SUBSCRIBE:
                return BasicResponse().response()
            elif Event == EVENT_UNSUBSCRIBE:
                return BasicResponse().response()
            else:
                return BasicResponse.response()
        else:
            return BasicResponse().response()


class MessageUtil(object):

    """Tools to transfer xml and string format messages.

    Wechat server POST the xml format message to django server,
    And django server need to POST xml format message to wechat server too.
    Define the message type, and get the message with xml format and parser it.
    """

    @staticmethod
    def parse_xml(xml_content):
        """Parse receive message with xml format from wechat server."""
        str_xml = xml_content.decode(u'utf-8')
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
