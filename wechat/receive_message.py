#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Receive message from wechat server to django server.

Copyright (C) 2016 Canux CHENG.
All rights reserved.
Name: receive_message.py
Author: Canux CHENG canuxcheng@gmail.com
Version: V1.0.0.0
Time: Tue 11 Oct 2016 12:22:40 AM EDT

Details:
    check the wechat doc, just support 6 kinds of message types.
"""


class BasicReceive(object):

    """Basic class for receive message.

    All message django server send to wechat server must have this four arguments.
    Wechat Just support send [text, image, voice, video, music, news].
    """

    def __init__(self):
        """Init some definition for message types."""
        # Receive/request message type from wechat user.
        REQ_MESSAGE_TYPE_TEXT = u'text'
        REQ_MESSAGE_TYPE_IMAGE = u'image'
        REQ_MESSAGE_TYPE_VOICE = u'voice'
        REQ_MESSAGE_TYPE_VIDEO = u'video'
        REQ_MESSAGE_TYPE_LOCATION = u'location'
        REQ_MESSAGE_TYPE_LINK = u'link'
        REQ_MESSAGE_TYPE_EVENT = u'event'

        # All send message have this arguments.
        self.to_user_name = u''
        self.from_user_name = u''
        self.create_time = 0L
        self.msg_type = u''
        self.msg_id = 0L

    def get_to_user_name(self):
        return self.to_user_name

    def set_to_user_name(self, to_user_name):
        self.to_user_name = to_user_name

    def get_from_user_name(self):
        return self.from_user_name

    def set_from_user_name(self, from_user_name):
        self.from_user_name = from_user_name

    def get_create_time(self):
        return self.create_time

    def set_create_time(self, create_time):
        self.create_time = create_time

    def get_msg_type(self):
        return self.msg_type

    def set_msg_type(self, msg_type):
        self.msg_type = msg_type

    def get_msg_id(self):
        return self.mgs_id

    def set_msg_id(self, msg_id):
        self.msg_id = msg_id
