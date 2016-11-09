#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SUMMARY

Copyright (C) 2016 Canux CHENG.
All rights reserved.
Name: text_parse_xml.py
Author: Canux CHENG canuxcheng@gmail.com
Version: V1.0.0.0
Time: Thu 13 Oct 2016 09:48:06 AM EDT

DETAILS:
"""
import codecs
from lxml import etree

f = codecs.open(u'test.xml', u'r', u'utf-8')
content = u"".join(f.readlines())
f.close()

req_xml = etree.fromstring(content.decode(u'utf-8'))
dict_xml = {}
for node0 in req_xml:
    dict_tmp0 = {}
    for node1 in node0.getchildren():
        dict_tmp0[node1.tag] = node1.text
    if any(dict_tmp0):
        dict_xml[node0.tag] = dict_tmp0
    else:
        dict_xml[node0.tag] = node0.text
print dict_xml
