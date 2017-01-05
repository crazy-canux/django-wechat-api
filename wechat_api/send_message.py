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

发送消息需要获取access_token和对应的url。

三种消息可以通过http的POST发送给用户：
    1. 客服消息
    2. 群发消息
    3. 模板消息
"""
