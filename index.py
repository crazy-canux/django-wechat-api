#!/usr/bin/env python
# -*- coding:utf-8 -*-
from wechat import wsgi
from bae.core.wsgi import WSGIApplication

application = WSGIApplication(wsgi.application)
