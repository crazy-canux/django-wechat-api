#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SUMMARY

Copyright (C) 2016 Canux CHENG.
All rights reserved.
Name: test_to_xml.py
Author: Canux CHENG canuxcheng@gmail.com
Version: V1.0.0.0
Time: Thu 13 Oct 2016 10:34:21 AM EDT

DETAILS:
"""
from django.conf import settings
settings.configure()

import sys
sys.path.append("../")

import time

from wechat.views import MessageUtil, RESP_MESSAGE_TYPE_TEXT
from wechat.send_message import Text
from wechat.image_how_old import image_how_old

send_text_object = Text()
send_text_object.set_to_user_name("canux")
send_text_object.set_from_user_name("wechat")
send_text_object.set_create_time(time.time())
send_text_object.set_msg_type(RESP_MESSAGE_TYPE_TEXT)

send_text_content = image_how_old("http://pic.cnr.cn/pic/guoji/20161013/W020161013487678057091.jpg")
send_text_object.set_content(send_text_content)

send_xml = MessageUtil.to_xml(send_text_object)
print send_xml
