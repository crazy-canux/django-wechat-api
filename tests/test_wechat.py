#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SUMMARY

Copyright (C) 2016 Canux CHENG.
All rights reserved.
Name: test_wechat.py
Author: Canux CHENG canuxcheng@gmail.com
Version: V1.0.0.0
Time: Thu 13 Oct 2016 09:51:26 AM EDT

DETAILS:
"""
import codecs

# TPL
import requests

f = codecs.open(u'test.xml', u'r', u'utf-8')
content = u''.join(f.readlines())
f.close()

url = "http://127.0.0.1:8000/wechat/"
result = requests.post(url, data=content.encode(u'utf-8'))
print result.text
