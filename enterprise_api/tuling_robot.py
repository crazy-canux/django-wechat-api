#!/usr/bin/env python
# -*- coding: utf-8 -*-
u"""
When got text message from wechat user, reply with tuling robot.

Copyright (C) 2016 Canux CHENG.
All rights reserved.
Name: tuling_robot.py
Author: Canux CHENG canuxcheng@gmail.com
Version: V1.0.0.0
Time: Sun 16 Oct 2016 01:53:46 AM EDT

DESCRIPTION:
    图灵机器人接口。

    http://www.tuling123.com
    Read the doc from tuling website.
    Use json format and HTTP POST to post data to tuling and return data with json format.
    Close the secret function for tuling robot.

    Send to tuling:
        {
            "key": "APIKEY",
            "info": "Your content",
            "userid": "wechat user openid(FromUserName), not support for booking account."
        }

    Receive from tuling:
        {
            "code": "your code",
            "text": "your content",
            "url": "url for link",

            "list": [
            {
                "article": "article1 for news",
                "source": "news from where",
                "icon": "",
                "detailurl": "url for news"
            },
            ...
            ],

            "list": [
            {
                "name": "food name for cookbook",
                "icon": "",
                "info": "food information.",
                "detailurl": "url for cookbook"
            },
            ...
            ]
        }

    code means what kind of message you got from tuling:
        100000: text
        200000: link
        302000: news
        308000: cookbok

"""
import json

# TPL
import requests

# Define tuling API.
TULING_API = "http://www.tuling123.com/openapi/api"
TULING_APIKEY = "b4987475ebed4c4c9684237ffc1d6dc0"


def tuling_robot(info, userid):
    """Send message and userid to tuling and get response.

    @param info: send the information to tuling123.
    @type info: unicode

    @param userid: the user id used for context.
    @type userid: int

    @returns resp_content: Response information from tuling123.
    @rtype resp_content: unicode

    send utf-8 to tuling, and return unicode.
    """
    s = requests.session()
    data = {"key": TULING_APIKEY, "info": info.encode("utf-8"), "userid": userid.encode("utf-8")}
    data = json.dumps(data)
    response = s.post(TULING_API, data=data)
    resp_data = json.loads(response.content)
    # print("resp_data: %s" % resp_data)
    code = resp_data['code']
    # print("code: %d" % code)
    # text = resp_data['text'].replace('<br>', '\n')
    if code == 100000:
        resp_content = resp_data['text']
    elif code == 200000:
        resp_content = resp_data['text'] + resp_data['url']
    elif code == 302000:
        resp_content = resp_data['text'] + resp_data['list'][0]['article'] + resp_data['list'][0]['source'] + resp_data['list'][0]['detailurl']
    elif code == 308000:
        resp_content = resp_data['text'] + resp_data['list'][0]['name'] + + resp_data['list'][0]['info'] + resp_data['list'][0]['detailurl']
    else:
        resp_content = u"听不懂鸟语，请说人话"
    return resp_content


def handle_tuling_robot(info, userid):
    try:
        resp_content = tuling_robot(info, userid)
    except Exception as e:
        # resp_content = "Debug: %s" % e
        resp_content = u''
    finally:
        return resp_content

if __name__ == "__main__":
    content = u"武汉"
    resp_content = handle_tuling_robot(content, '1234')
    print("type: %s\ncontent: %s" % (type(resp_content), resp_content))
