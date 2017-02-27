#!/usr/bin/env python
# -*- coding: utf-8 -*-
u"""
Use http://how-old.net to analyze the sex and age of the picture.

Copyright (C) 2016 Canux CHENG.
All rights reserved.
Name: how_old.py
Author: Canux CHENG canuxcheng@gmail.com
Version: V1.0.0.0
Time: Mon 10 Oct 2016 12:45:48 AM EDT

DESCRIPTION:
    使用MicroSoft的how-old.net网站获取图片中人物的性别和年龄。
"""
import re

# TPL
import requests


def how_old(image_url):
    """Get the sex and age from how-old.net.

    @param image_url: specify the image.
    @type image_url: str
    @returns resp_content: response from how-old.net.
    @rtype resp_content: unicode

    The image must be a human.
    """
    s = requests.session()
    url = "http://how-old.net/Home/Analyze?isTest=False&source=&version=001"
    header = {
        "Accept-Encoding": "gzip, deflate",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0",
        "Host": "how-old.net",
        "Referer": "http://how-old.net/",
        "X-Requested-With": "XMLHttpRequest"
    }
    data = {"file": s.get(image_url).content}
    r = s.post(url, files=data, headers=header)
    #print("r: %s\n\n\n" % r)
    h = r.content
    #print("h: %s\n\n\n" % h)
    i = h.replace('\\', '')
    #print("i: %s\n\n\n" % i)

    gender = re.search(r'"gender": "(.*?)"rn', i)
    age = re.search(r'"age": (.*?),rn', i)
    if gender.group(1) == "Male":
        gender_zh = u"男"
    else:
        gender_zh = u"女"
    datas = [gender_zh, age.group(1)]
    #print("datas: {}".format(datas))
    resp_content = u'图中人物性别为' + datas[0] + '\n' + u'年龄为' + datas[1]
    #print(resp_content)
    return resp_content


def handle_how_old(image_url):
    try:
        resp_content = how_old(image_url)
    except Exception as e:
        #resp_content = 'Debug: %s' % e
        resp_content = u''
    finally:
        return resp_content

if __name__ == "__main__":
    url = "http://pic.cnr.cn/pic/guoji/20161013/W020161013487678057091.jpg"
    # url = "http://pic.cnr.cn/pic/yc/20160810/W020160810375887124990.jpg"
    resp_content = handle_how_old(url)
    print("type: %s\n content: %s" % (type(resp_content), resp_content))
