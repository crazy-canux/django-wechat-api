#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Send message from django server to wechat server.

Copyright (C) 2016 Canux CHENG.
All rights reserved.
Name: send_message.py
Author: Canux CHENG canuxcheng@gmail.com
Version: V1.0.0.0
Time: Tue 11 Oct 2016 12:22:40 AM EDT

Details:
    check the wechat doc, just support 6 kinds of message types.
"""
import time


class Text(object):

    """Basic text object class."""

    def __init__(self, ToUserName, FromUserName, Content):
        self.__dict = dict()
        self.__dict["ToUserName"] = ToUserName
        self.__dict["FromUserName"] = FromUserName
        self.__dict["CreateTime"] = int(time.time())
        self.__dict["Content"] = Content

    def send(self):
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


class Image(object):

    """Basic Image object class."""

    def __init__(self, ToUserName, FromUserName, MediaId):
        self.__dict = dict()
        self.__dict["ToUserName"] = ToUserName
        self.__dict["FromUserName"] = FromUserName
        self.__dict["CreateTime"] = int(time.time())
        self.__dict["MediaId"] = MediaId

    def send(self):
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


class Voice(object):

    """Basic voice class."""

    def __init__(self, ToUserName, FromUserName, MediaId):
        self.__dict = dict()
        self.__dict["ToUserName"] = ToUserName
        self.__dict["FromUserName"] = FromUserName
        self.__dict["CreateTime"] = int(time.time())
        self.__dict["MediaId"] = MediaId

    def send(self):
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


class Video(object):

    """Basic video class."""

    def __init__(self, ToUserName, FromUserName, MediaId, Title, Description):
        self.__dict = dict()
        self.__dict["ToUserName"] = ToUserName
        self.__dict["FromUserName"] = FromUserName
        self.__dict["CreateTime"] = int(time.time())
        self.__dict["MediaId"] = MediaId
        self.__dict["Title"] = Title
        self.__dict["Description"] = Description

    def send(self):
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


class Music(object):

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

    def send(self):
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


class News(object):

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

    def send(self):
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
