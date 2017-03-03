#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sae

# For SAE to add third party libraries.
# $pip install -t site-packages -r requirements.txt
#import os
#import sys
#root = os.path.dirname(__file__)
#sys.path.insert(0, os.path.join(root, "site-packages"))
sae.add_vendor_dir("site-packages")

from wechat import wsgi

application = sae.create_wsgi_app(wsgi.application)
