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


@csrf_exempt
def wechat_varify(request):
    """Basic function used to communicate with wechat.

    GET means wechat server make connection with django server.
    POST means wechat user send message to wechat server and transfer to django server,
    And django server send message back to wechat server and transfer to wechat user.
    """
    if request.method == "GET":
        # Wechat server sent GET request to the URL to verify.
        print("Start to get")
        return HttpResponse(WechatRequest.get_request(request), content_type="text/plain")
    elif request.method == "POST":
        # Wechat user POST the message to the URL with XML format.
        print("Start to post")
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
        signature = request.GET.get("signature", None)
        timestamp = request.GET.get("timestamp", None)
        nonce = request.GET.get("nonce", None)
        echostr = request.GET.get("echostr", None)
        token = settings.WECHAT_TOKEN

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
            return None

    @staticmethod
    def post_request(request):
        request_map = MessageUtil.parse_xml(request)
        receive_basic_object = BasicReceive(request_map)
        MsgType = receive_basic_object.MsgType

        # Response to different request message type.
        if MsgType == REC_MESSAGE_TYPE_TEXT:
            return BasicResponse().response()
        elif MsgType == REC_MESSAGE_TYPE_IMAGE:
            return BasicResponse().response()
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
