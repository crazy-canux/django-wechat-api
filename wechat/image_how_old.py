#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Use http://how-old.net to analyze the sex and age of the picture.

Copyright (C) 2016 Canux CHENG.
All rights reserved.
Name: image_how_old.py
Author: Canux CHENG canuxcheng@gmail.com
Version: V1.0.0.0
Time: Mon 10 Oct 2016 12:45:48 AM EDT

DETAILS:
    The image must be a human.
"""
import re

import requests


def how_old(image_url):
    """Get the sex and age from how-old.net."""
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
    h = r.content
    i = h.replace('\\', '')

    gender = re.search(r'"gender": "(.*?)"rn', i)
    age = re.search(r'"age": (.*?),rn', i)
    if gender.group(1) == "Male":
        gender_zh = "男"
    else:
        gender_zh = "女"
    datas = [gender_zh, age.group(1)]
    return datas


def image_how_old(image_url):
    try:
        datas = how_old(image_url)
        resp_content = '图中人物性别为' + datas[0] + '\n' + '年龄为' + datas[1]
    except Exception:
        resp_content = '识别结果为人妖'
    finally:
        return resp_content

if __name__ == "__main__":
    print image_how_old("http://pic.cnr.cn/pic/guoji/20161013/W020161013487678057091.jpg")
