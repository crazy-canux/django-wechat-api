#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
URL for wechat.

Copyright (C) 2016 Canux CHENG.
All rights reserved.
Name: urls.py
Author: Canux CHENG canuxcheng@gmail.com
Version: V1.0.0.0
Time: Sun 09 Oct 2016 10:41:32 PM EDT
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.wechat_varify, name='wechat_varify'),
]
