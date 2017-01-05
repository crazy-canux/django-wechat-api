#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Response message through django server to wechat server when get message/event from wechat user.

Copyright (C) 2016 Canux CHENG.
All rights reserved.
Name: response_message.py
Author: Canux CHENG canuxcheng@gmail.com
Version: V1.0.0.0
Time: Tue 11 Oct 2016 12:22:40 AM EDT

DESCRIPTION:
    当收到用户发送的消息或事件，django后台对此进行回复的消息类型。
"""
import time


class BasicResponse(object):

    u"""If django server can not response in 5 seconds, must reply 'success' or NULL and wechat server have 3 times to retry.

    如果django后台不能及时响应，需要回复"success"或者空字符串，否则wechat服务器会发送"该公众号暂时无法提供服务，请稍后再试"给用户。
    """

    def __init__(self):
        pass

    def response(self):
        return "success"


class Text(BasicResponse):

    """Basic text object class."""

    def __init__(self, ToUserName, FromUserName, Content):
        self.__dict = dict()
        self.__dict["ToUserName"] = ToUserName
        self.__dict["FromUserName"] = FromUserName
        self.__dict["CreateTime"] = int(time.time())
        self.__dict["Content"] = Content.encode("utf-8")

    def response(self):
        xml_form = """
        <xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[text]]></MsgType>
        <Content><![CDATA[{Content}]]></Content>
        </xml>
        """
        return xml_form.format(**self.__dict)


class Image(BasicResponse):

    """Basic Image object class."""

    def __init__(self, ToUserName, FromUserName, MediaId):
        self.__dict = dict()
        self.__dict["ToUserName"] = ToUserName
        self.__dict["FromUserName"] = FromUserName
        self.__dict["CreateTime"] = int(time.time())
        self.__dict["MediaId"] = MediaId

    def response(self):
        xml_form = """
        <xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[image]]></MsgType>
        <Image>
        <MediaId><![CDATA[{MediaId}]]></MediaId>
        </Image>
        </xml>
        """
        return xml_form.format(**self.__dict)


class Voice(BasicResponse):

    """Basic voice class."""

    def __init__(self, ToUserName, FromUserName, MediaId):
        self.__dict = dict()
        self.__dict["ToUserName"] = ToUserName
        self.__dict["FromUserName"] = FromUserName
        self.__dict["CreateTime"] = int(time.time())
        self.__dict["MediaId"] = MediaId

    def response(self):
        xml_form = """
        <xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[voice]]></MsgType>
        <Voice>
        <MediaId><![CDATA[{MediaId}]]></MediaId>
        </Voice>
        </xml>
        """
        return xml_form.format(**self.__dict)


class Video(BasicResponse):

    """Basic video class."""

    def __init__(self, ToUserName, FromUserName, MediaId, Title, Description):
        self.__dict = dict()
        self.__dict["ToUserName"] = ToUserName
        self.__dict["FromUserName"] = FromUserName
        self.__dict["CreateTime"] = int(time.time())
        self.__dict["MediaId"] = MediaId
        self.__dict["Title"] = Title
        self.__dict["Description"] = Description

    def response(self):
        xml_form = """
        <xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[video]]></MsgType>
        <Video>
        <MediaId><![CDATA[{MediaId}]]></MediaId>
        <Title><![CDATA[{Title}]]></Title>
        <Description><![CDATA[{Description}]]></Description>
        </Video>
        </xml>
        """
        return xml_form.format(**self.__dict)


class Music(BasicResponse):

    """Basic music class."""

    def __init__(self, ToUserName, FromUserName, Title, Description, MusicUrl, HQMusicUrl, ThumbMediaId):
        self.__dict = dict()
        self.__dict["ToUserName"] = ToUserName
        self.__dict["FromUserName"] = FromUserName
        self.__dict["CreateTime"] = int(time.time())
        self.__dict["Title"] = Title
        self.__dict["Description"] = Description
        self.__dict["MusicUrl"] = MusicUrl
        self.__dict["HQMusicUrl"] = HQMusicUrl
        self.__dict["ThumbMediaId"] = ThumbMediaId

    def response(self):
        xml_form = """
        <xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[music]]></MsgType>
        <Music>
        <Title><![CDATA[{Title}]]></Title>
        <Description><![CDATA[{Description}]]></Description>
        <MusicUrl><![CDATA[{MusicUrl}]]></MusicUrl>
        <HQMusicUrl><![CDATA[{HQMusicUrl}]]></HQMusicUrl>
        <ThumbMediaId><![CDATA[{ThumbMediaId}]]></ThumbMediaId>
        </Music>
        </xml>
        """
        return xml_form.format(**self.__dict)


class News(BasicResponse):

    """Basic news object class."""

    def __init__(self, ToUserName, FromUserName, ArticleCount, Title, Description, PicUrl, Url):
        self.__dict = dict()
        self.__dict["ToUserName"] = ToUserName
        self.__dict["FromUserName"] = FromUserName
        self.__dict["CreateTime"] = int(time.time())
        self.__dict["ArticleCount"] = ArticleCount
        self.__dict["Title"] = Title
        self.__dict["Description"] = Description
        self.__dict["PicUrl"] = PicUrl
        self.__dict["Url"] = Url

    def response(self):
        xml_form = """
        <xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[news]]></MsgType>
        <ArticleCount>{ArticleCount}</ArticleCount>
        <Articles>
        <item>
        <Title><![CDATA[{Title}]]></Title>
        <Description><![CDATA[{Description}]]></Description>
        <PicUrl><![CDATA[{PicUrl}]]></PicUrl>
        <Url><![CDATA[{Url}]]></Url>
        </item>
        </Articles>
        </xml>
        """
        return xml_form.format(**self.__dict)
