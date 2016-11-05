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


class BasicSend(object):

    """If django server can not response in 5 seconds, must reply 'success' or NULL and wechat server have 3 times to retry.

    So, If you don't want to reply this kinds of receive message, just reply 'success' to tell wechat server you already know.
    Or wechat will reply '该公众号暂时无法提供服务，请稍后再试' automatic.
    """

    def __init__(self):
        pass

    def send(self):
        return "success"


class Text(BasicSend):

    """Basic text object class."""

    def __init__(self, ToUserName, FromUserName, Content):
        self.__dict = dict()
        self.__dict["ToUserName"] = ToUserName
        self.__dict["FromUserName"] = FromUserName
        self.__dict["CreateTime"] = int(time.time())
        self.__dict["Content"] = Content.encode("utf-8")

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


class Image(BasicSend):

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


class Voice(BasicSend):

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


class Video(BasicSend):

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


class Music(BasicSend):

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


class News(BasicSend):

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
