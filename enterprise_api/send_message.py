#!/usr/bin/env python
# -*- coding: utf-8 -*-
u"""
Send message from django server to wechat server(wechat user).

Copyright (C) 2016 Canux CHENG.
All rights reserved.
Name: send_message.py
Author: Canux CHENG canuxcheng@gmail.com
Version: V1.0.0.0
Time: Sun 13 Nov 2016 01:58:36 AM EST

主动发送消息需要获取access_token和对应的url。

没有实现的消息类型：
1. news
2. mpnews
"""
from django.conf import settings

AGENT_ID = settings.AGENTID
SAFE = settings.SAFE


class SendText(object):

    """Send text message to wechat user."""

    def __init__(self, touser, toparty, totag, content):
        self.__dict = dict()
        self.__dict['touser'] = touser
        self.__dict['toparty'] = toparty
        self.__dict['totag'] = totag
        self.__dict['agentid'] = AGENT_ID
        self.__dict['safe'] = SAFE
        self.__dict['content'] = content

    def send(self):
        json_form = """
        {
            "touser": {touser},
            "toparty": {toparty},
            "totag": {totag},
            "msgtype": "text",
            "agentid": {agentid},
            "text": {
                "content": {content}
            },
            "safe": {safe}
        }"""
        return json_form.format(**self.__dict)


class SendImage(object):

    """Send image message to wechat user."""

    def __init__(self, touser, toparty, totag, media_id):
        self.__dict = dict()
        self.__dict['touser'] = touser
        self.__dict['toparty'] = toparty
        self.__dict['totag'] = totag
        self.__dict['agentid'] = AGENT_ID
        self.__dict['safe'] = SAFE
        self.__dict['media_id'] = media_id

    def send(self):
        json_form = """
        {
            "touser": {touser},
            "toparty": {toparty},
            "totag": {totag},
            "msgtype": "image",
            "agentid": {agentid},
            "image": {
                "media_id": {media_id}
            },
            "safe": {safe}
        }"""
        return json_form.format(**self.__dict)


class SendVoice(object):

    """Send voice message to wechat user."""

    def __init__(self, touser, toparty, totag, media_id):
        self.__dict = dict()
        self.__dict['touser'] = touser
        self.__dict['toparty'] = toparty
        self.__dict['totag'] = totag
        self.__dict['agentid'] = AGENT_ID
        self.__dict['safe'] = SAFE
        self.__dict['media_id'] = media_id

    def send(self):
        json_form = """
        {
            "touser": {touser},
            "toparty": {toparty},
            "totag": {totag},
            "msgtype": "image",
            "agentid": {agentid},
            "image": {
                "media_id": {media_id}
            },
            "safe": {safe}
        }"""
        return json_form.format(**self.__dict)


class SendVideo(object):

    """Send video message to wechat user."""

    def __init__(self, touser, toparty, totag, media_id, title, description):
        self.__dict = dict()
        self.__dict['touser'] = touser
        self.__dict['toparty'] = toparty
        self.__dict['totag'] = totag
        self.__dict['agentid'] = AGENT_ID
        self.__dict['safe'] = SAFE
        self.__dict['media_id'] = media_id
        self.__dict['title'] = title
        self.__dict['description'] = description

    def send(self):
        json_form = """
        {
            "touser": {touser},
            "toparty": {toparty},
            "totag": {totag},
            "msgtype": "video",
            "agentid": {agentid},
            "video": {
                "media_id": {media_id},
                "title": {title},
                "description": {description}
            },
            "safe": {safe}
        }"""
        return json_form.format(**self.__dict)


class SendFile(object):

    """Send file message to wechat user."""

    def __init__(self, touser, toparty, totag, media_id):
        self.__dict = dict()
        self.__dict['touser'] = touser
        self.__dict['toparty'] = toparty
        self.__dict['totag'] = totag
        self.__dict['agentid'] = AGENT_ID
        self.__dict['safe'] = SAFE
        self.__dict['media_id'] = media_id

    def send(self):
        json_form = """
        {
            "touser": {touser},
            "toparty": {toparty},
            "totag": {totag},
            "msgtype": "file",
            "agentid": {agentid},
            "file": {
                "media_id": {media_id}
            },
            "safe": {safe}
        }"""
        return json_form.format(**self.__dict)
