#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Get access_token.

Copyright (C) 2016 Canux CHENG.
All rights reserved.
Name: access_token.py
Author: Canux CHENG canuxcheng@gmail.com
Version: V1.0.0.0
Time: Mon 07 Nov 2016 08:37:21 AM EST

DESCRIPTION:
    1. access_token

    access_token是公众号的全局唯一接口调用凭据，公众号调用各接口时都需使用access_token。
    公众号可以使用AppID和AppSecret调用本接口来获取access_token。

    http请求方式:
        GET
        https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=APPID&secret=APPSECRET
        grant_type  是  获取access_token填写client_credential
        appid       是  第三方用户唯一凭证
        secret      是  第三方用户唯一凭证密钥，即appsecret

    正常情况下，微信会返回下述JSON数据包给公众号：
        {"access_token":"ACCESS_TOKEN","expires_in":7200}
        access_token    获取到的凭证
        expires_in  凭证有效时间，单位：秒

    错误时微信会返回错误码等信息，JSON数据包示例如下（该示例为AppID无效错误）:
        {"errcode":40013,"errmsg":"invalid appid"}

    2. IP
    如果公众号基于安全等考虑，需要获知微信服务器的IP地址列表，以便进行相关限制，可以通过该接口获得微信服务器IP地址列表或者IP网段信息。

    http请求方式:
        GET
        https://api.weixin.qq.com/cgi-bin/getcallbackip?access_token=ACCESS_TOKEN
        access_token    是  公众号的access_token

    正常情况下，微信会返回下述JSON数据包给公众号：
        {
            "ip_list": [
                "127.0.0.1",
                "127.0.0.2",
                "101.226.103.0/25"
            ]
        }
        ip_list 微信服务器IP地址列表

    错误时微信会返回错误码等信息，JSON数据包示例如下（该示例为AppID无效错误）:
        {"errcode":40013,"errmsg":"invalid appid"}
"""
from django.con import settings

import json

# TPL
import requests

class Basic(object):

    """Basic class for access_token."""

    def __init__(self):
        self.access_token = ''
        self.expires_in = ''

    def refresh_access_token(self):
        url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s" % (settings.WECHAT_APP_ID, settings.WECHAT_APP_SECRET)
        r = requests.get(url)
        dict_data = json.loads(r.content)
        self.access_token = dict_data['access_token']
        self.expires_in = dict_data['expires_in']

    def get_access_token(self):
        if self.expires_in < 10:
            self.refresh_access_token()
        return self.access_token
