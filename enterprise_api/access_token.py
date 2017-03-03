#!/usr/bin/env python
# -*- coding: utf-8 -*-
u"""
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
    企业号可以使用CorpID和Secret调用本接口来获取access_token。

    http请求方式:
        GET
        https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=id&corpsecret=secrect
        corpid  是  企业Id,每个企业号唯一。
        corpsecret  是  管理组的凭证密钥, 每个管理组一个。

    正常情况下，微信会返回下述JSON数据包给公众号：
        {"access_token":"ACCESS_TOKEN","expires_in":7200}
        access_token    获取到的凭证, 长度为64至512个字节,不同的管理组不同。
        expires_in  凭证有效时间，单位：秒

    错误时微信会返回错误码等信息，JSON数据包示例如下（该示例为AppID无效错误）:
        {"errcode":40013,"errmsg":"invalid appid"}

    2. IP
    获取wechat服务器的IP

    http请求方式:
        GET
        https://qyapi.weixin.qq.com/cgi-bin/getcallbackip?access_token=ACCESS_TOKEN
        access_token    是  调用接口凭证

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
from django.conf import settings

import json

# TPL
import requests

ENTERPRISE_CORPID = settings.CORPID
ENTERPRISE_SECRET = settings.SECRET


class AccessToken(object):

    """Basic class for access_token."""

    def __init__(self):
        self.access_token = ''
        self.expires_in = 0

    def refresh_access_token(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=%s&corpsecret=%s" % (ENTERPRISE_CORPID, ENTERPRISE_SECRET)
        r = requests.get(url)
        dict_data = json.loads(r.content)
        print(dict_data)
        self.access_token = dict_data['access_token']
        self.expires_in = dict_data['expires_in']

    def get_access_token(self):
        if self.expires_in < 10:
            self.refresh_access_token()
        return self.access_token


if __name__ == "__main__":
    at = AccessToken()
    access_token = at.get_access_token()
    print(access_token)
