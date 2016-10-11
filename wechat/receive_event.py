#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Receive event message from wechat server to django server.

Copyright (C) 2016 Canux CHENG.
All rights reserved.
Name: receive_event.py
Author: Canux CHENG canuxcheng@gmail.com
Version: V1.0.0.0
Time: Tue 11 Oct 2016 12:50:44 AM EDT
"""


class BasicEvent(object):

    """Basic event object class."""

    def __init__(self):
        # Event type from wechat user.
        EVENT_TYPE_SUBSCRIBE = u'subscribe'
        EVENT_TYPE_UNSUBSCRIBE = u'unsubscribe'
        EVENT_TYPE_LOCATION = u'location'
        EVENT_TYPE_CLICK = u'click'
        EVENT_TYPE_VIEW = u'view'
        EVENT_TYPE_SCAN = u'scan'
        # Scan with tips
        EVENT_TYPE_SCANCODE_WAITMSG = u'scancode_waitmsg'
        # Scan push event
        EVENT_TYPE_SCANCODE_PUSH = U'scancode_push'

        # All send message have this arguments.
        self.to_user_name = u''
        self.from_user_name = u''
        self.create_time = 0L
        self.msg_type = u''
        self.msg_id = 0L
        # All event have this arguments.
        self.to_user_name = u''
        self.from_user_name = u''
        self.create_time = 0L
        self.msg_type = u''
        self.event = u''

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

    def get_event(self):
        return self.event

    def set_event(self, event):
        self.event = event
