#!/usr/bin/env python
# -*- coding: utf-8 -*-
u"""
Wechat user send message to wechat server and transfer to django server.

Copyright (C) 2016 Canux CHENG.
All rights reserved.
Name: receive_message.py
Author: Canux CHENG canuxcheng@gmail.com
Version: V1.0.0.0
Time: Fri 14 Oct 2016 11:04:21 AM EDT

DESCRIPTION:
    wechat用户通过http的post发送给企业服务器的经过解密后的消息类型格式。
"""


class BasicReceive(object):

    """Basic class for reveive message."""

    def __init__(self, msg_dict):
        self.ToUserName = msg_dict.get("ToUserName")
        self.FromUserName = msg_dict.get("FromUserName")
        self.CreateTime = msg_dict.get("CreateTime")
        self.MsgType = msg_dict.get("MsgType")
        self.MsgId = msg_dict.get("MsgId")
        self.AgentID = msg_dict.get("AgentID")


class TextMsg(BasicReceive):

    """Basic class for receive text message.

    <xml>
    <ToUserName><![CDATA[toUser]]></ToUserName>
    <FromUserName><![CDATA[fromUser]]></FromUserName>
    <CreateTime>1348831860</CreateTime>
    <MsgType><![CDATA[text]]></MsgType>
    <Content><![CDATA[this is a text]]></Content>
    <MsgId>1234567890123456</MsgId>
    <AgentID>1</AgentID>
    </xml>

    @param self.Content
    @type unicode
    """

    def __init__(self, msg_dict):
        super(TextMsg, self).__init__(msg_dict)
        self.Content = msg_dict.get("Content")


class ImageMsg(BasicReceive):

    """Basic class for receive image message.

    <xml>
    <ToUserName><![CDATA[toUser]]></ToUserName>
    <FromUserName><![CDATA[fromUser]]></FromUserName>
    <CreateTime>1348831860</CreateTime>
    <MsgType><![CDATA[image]]></MsgType>
    <PicUrl><![CDATA[this is a url]]></PicUrl>
    <MediaId><![CDATA[media_id]]></MediaId>
    <MsgId>1234567890123456</MsgId>
    <AgentID>1</AgentID>
    </xml>
    """

    def __init__(self, msg_dict):
        super(ImageMsg, self).__init__(msg_dict)
        self.PicUrl = msg_dict.get("PicUrl")
        self.MediaId = msg_dict.get("MediaID")


class VoiceMsg(BasicReceive):

    u"""Basic class for receive voice message.

    <xml>
    <ToUserName><![CDATA[toUser]]></ToUserName>
    <FromUserName><![CDATA[fromUser]]></FromUserName>
    <CreateTime>1357290913</CreateTime>
    <MsgType><![CDATA[voice]]></MsgType>
    <MediaId><![CDATA[media_id]]></MediaId>
    <Format><![CDATA[Format]]></Format>
    <Recognition><![CDATA[腾讯微信团队]]></Recognition>
    <MsgId>1234567890123456</MsgId>
    <AgentID>1</AgentID>
    </xml>
    """

    def __init__(self, msg_dict):
        super(VoiceMsg, self).__init__(msg_dict)
        self.MediaId = msg_dict.get("MediaId")
        self.Format = msg_dict.get("Format")
        self.Recognition = msg_dict.get("Recognition")


class VideoMsg(BasicReceive):

    """Basic class for receive video message.

    <xml>
    <ToUserName><![CDATA[toUser]]></ToUserName>
    <FromUserName><![CDATA[fromUser]]></FromUserName>
    <CreateTime>1357290913</CreateTime>
    <MsgType><![CDATA[video]]></MsgType>
    <MediaId><![CDATA[media_id]]></MediaId>
    <ThumbMediaId><![CDATA[thumb_media_id]]></ThumbMediaId>
    <MsgId>1234567890123456</MsgId>
    <AgentID>1</AgentID>
    </xml>
    """

    def __init__(self, msg_dict):
        super(VideoMsg, self).__init__(msg_dict)
        self.MediaId = msg_dict.get("MsgId")
        self.ThumbMediaId = msg_dict.get("ThumbMediaId")


class ShortVideoMsg(BasicReceive):

    """Basic class for receive shortvideo message.

    <xml>
    <ToUserName><![CDATA[toUser]]></ToUserName>
    <FromUserName><![CDATA[fromUser]]></FromUserName>
    <CreateTime>1357290913</CreateTime>
    <MsgType><![CDATA[shortvideo]]></MsgType>
    <MediaId><![CDATA[media_id]]></MediaId>
    <ThumbMediaId><![CDATA[thumb_media_id]]></ThumbMediaId>
    <MsgId>1234567890123456</MsgId>
    <AgentID>1</AgentID>
    </xml>
    """

    def __init__(self, msg_dict):
        super(ShortVideoMsg, self).__init__(msg_dict)
        self.MediaId = msg_dict.get("MsgId")
        self.ThumbMediaId = msg_dict.get("ThumbMediaId")


class LocationMsg(BasicReceive):

    u"""Basic class for receive location message.

    <xml>
    <ToUserName><![CDATA[toUser]]></ToUserName>
    <FromUserName><![CDATA[fromUser]]></FromUserName>
    <CreateTime>1351776360</CreateTime>
    <MsgType><![CDATA[location]]></MsgType>
    <Location_X>23.134521</Location_X>
    <Location_Y>113.358803</Location_Y>
    <Scale>20</Scale>
    <Label><![CDATA[位置信息]]></Label>
    <MsgId>1234567890123456</MsgId>
    <AgentID>1</AgentID>
    </xml>
    """

    def __init__(self, msg_dict):
        super(LocationMsg, self).__init__(msg_dict)
        self.Location_X = msg_dict.get("Location_X")
        self.Location_Y = msg_dict.get("Location_Y")
        self.Scale = msg_dict.get("Scale")
        self.Label = msg_dict.get("Label")


class LinkMsg(BasicReceive):

    u"""Basic class for receive link message.

    <xml>
    <ToUserName><![CDATA[toUser]]></ToUserName>
    <FromUserName><![CDATA[fromUser]]></FromUserName>
    <CreateTime>1351776360</CreateTime>
    <MsgType><![CDATA[link]]></MsgType>
    <Title><![CDATA[公众平台官网链接]]></Title>
    <Description><![CDATA[公众平台官网链接]]></Description>
    <Url><![CDATA[url]]></Url>
    <MsgId>1234567890123456</MsgId>
    <AgentID>1</AgentID>
    </xml>
    """

    def __init__(self, msg_dict):
        super(LinkMsg, self).__init__(msg_dict)
        self.Title = msg_dict.get("Title")
        self.Description = msg_dict.get("Description")
        self.Url = msg_dict.get("Url")
