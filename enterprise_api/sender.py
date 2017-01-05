#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Send message to wechat user.

Copyright (C) 2016 Canux CHENG.
All rights reserved.
Name: sender.py
Author: Canux CHENG canuxcheng@gmail.com
Version: V1.0.0.0
Time: Tue 15 Nov 2016 09:18:16 AM EST

DESCRIPTION:
    URL = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=ACCESS_TOKEN"
    收件人必须处于应用的可见范围内，并且管理组对应用有使用权限、对收件人有查看权限，否则本次调用失败。

    如果无权限或收件人不存在，则本次发送失败；如果未关注，发送仍然执行。两种情况下均返回无效的部分:
        {
           "errcode": 0,
           "errmsg": "ok",
           "invaliduser": "UserID1",
           "invalidparty":"PartyID1",
           "invalidtag":"TagID1"
        }
"""



