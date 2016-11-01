.. image:: https://img.shields.io/pypi/v/nine.svg?style=plastic
   :target: https://pypi.python.org/pypi/pydjangowechat/1.0.0.0

==============
pydjangowechat
==============

pydjangowechat is a pure python project based on django.

This project is for Wechat Official Accounts API.

`[Wechat-Interface] <https://mp.weixin.qq.com/wiki/home/>`_

==========
How to use
==========

Install django application pydjangowechat::

    pip install pydjangowechat

Put your configuration in your django project in settings.py::

    INSTALLED_APPS = (
    ...
    'pydjangowechat'
    )

    MYSQL_DB = 'wechat'
    MYSQL_USER = 'django'
    MYSQL_PASS = '******'
    MYSQL_HOST = 'localhost'
    MYSQL_PORT = '3306'

    WECHAT_TOKEN = u'your_token'
    WECHAT_APP_ID = u'your_app_id'
    WECHAT_APP_SECRET = u'your_app_secret'

====
Test
====

Create a django project "wechat" and wechat account "xFullStack".

Deploy this project on Sina SAE platform for test.

pydjangowechat/wechat is the django project for test.

---
SAE
---

SAE is sina cloud platform.

pydjangowechat/site-packages is the third party libraries for SAE.

pydjangowechat/config.yaml is for SAE.

pydjangowechat/index.wsgi is for SAE.

pydjangowechat/wechat.sql is for SAE Mysql.

`[Sina-SAE] <http://www.sinacloud.com/doc/sae/python/index.html>`_

----------
xFullStack
----------

xFullStack is the test Wechat Official Accounts.

.. figure:: /data/xfullstack.jpg
   :alt: pic

====
TODO
====

1. Create menu.

============
Contribution
============

`Contribution <CONTRIBUTING.md>`__

=======
Authors
=======

`Authors <AUTHORS.md>`__

=======
License
=======

`License <LICENSE>`__
