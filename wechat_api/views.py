# -*- coding: utf-8 -*-
# from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.conf import settings

import hashlib

# TPL
from lxml import etree

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
EVENT_SCAN = u'SCAN'
EVENT_LOCATION = u'LOCATION'
EVENT_CLICK = u'CLICK'
EVENT_VIEW = u'VIEW'

# Response message types to wechat user.
RESP_MESSAGE_TYPE_TEXT = u'text'
RESP_MESSAGE_TYPE_IMAGE = u'image'
RESP_MESSAGE_TYPE_VOICE = u'voice'
RESP_MESSAGE_TYPE_VIDEO = u'video'
RESP_MESSAGE_TYPE_MUSIC = u'music'
RESP_MESSAGE_TYPE_NEWS = u'news'
MESSAGE_TYPE = [u'text', u'image', u'voice', u'video', u'music', u'news']

# 订阅号或服务号的token
TOKEN = settings.WECHAT_TOKEN


@csrf_exempt
def wechat_varify(request):
    """Basic function used to conmunicate with wechat.

    GET means wechat server make connection with django server.
    POST means wechat user send message to wechat server and transfer to django server,
    And django server response message back to wechat server and transfer to wechat user.
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
        u"""Wechat server use http GET to make connect with django server.

        将token、timestamp、nonce三个参数进行字典序排序
        将三个参数字符串拼接成一个字符串进行sha1加密
        开发者获得加密后的字符串可与signature对比，标识该请求来源于微信
        """
        signature = request.GET.get("signature", None)
        timestamp = request.GET.get("timestamp", None)
        nonce = request.GET.get("nonce", None)
        echostr = request.GET.get("echostr", None)
        token = TOKEN

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
            return echostr
        else:
            return None

    @staticmethod
    def post_request(request):
        """When get message or event from wechat user(wechat server), django server response something.

        This is just reply the message and event.
        Not django server use http to post message to wechat server(wechat user).
        """
        request_map = MessageUtil.parse_xml(request)
        receive_basic_object = BasicReceive(request_map)
        MsgType = receive_basic_object.MsgType
        ToUserName = receive_basic_object.ToUserName
        FromUserName = receive_basic_object.FromUserName

        # Response to different request message type.
        if MsgType == REC_MESSAGE_TYPE_TEXT:
            receive_text_object = TextMsg(request_map)
            receive_content = receive_text_object.Content
            response_content = handle_tuling_robot(receive_content, FromUserName)
            # If return nothing from tuling robot.
            if not response_content:
                response_content = u"只识别人话哦，别说鸟语!"
            response_text_object = Text(FromUserName, ToUserName, response_content)
            return response_text_object.response()
        elif MsgType == REC_MESSAGE_TYPE_IMAGE:
            receive_image_object = ImageMsg(request_map)
            PicUrl = receive_image_object.PicUrl
            response_content = handle_how_old(PicUrl)
            # If return nothing from how-old.net.
            if not response_content:
                response_content = u"只识别男女哦，不要发人妖!"
            response_image_object = Text(FromUserName, ToUserName, response_content)
            return response_image_object.response()
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
            return BasicResponse().response()
            Event = request_map.get(u'Event')
            if Event == EVENT_SUBSCRIBE:
                return BasicResponse().response()
            elif Event == EVENT_UNSUBSCRIBE:
                return BasicResponse().response()
            elif Event == EVENT_SCAN:
                return BasicResponse().response()
            elif Event == EVENT_LOCATION:
                return BasicResponse().response()
            elif Event == EVENT_CLICK:
                return BasicResponse().response()
            elif Event == EVENT_VIEW:
                return BasicResponse().response()
            else:
                return BasicResponse().response()
        else:
            return BasicResponse().response()


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
