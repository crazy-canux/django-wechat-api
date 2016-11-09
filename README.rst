.. image::
    https://img.shields.io/pypi/v/django-wechat-api.svg?style=plastic
   :target: https://pypi.python.org/pypi/django-wechat-api/

.. image:: https://img.shields.io/pypi/dm/django-wechat-api.svg?style=plastic
   :target: https://pypi.python.org/pypi/django-wechat-api/

=======
Project
=======

wechat is a django project created for test wechat API applications.

===========
Application
===========

- wechat_api

  This django application is the API for wechat subscribe and service account.

`[Wechat-Interface] <https://mp.weixin.qq.com/wiki/home/>`_

- enterprise_api

  This django application is the API for wechat enterprise account.

`[Enterprise-Interface] <http://qydev.weixin.qq.com/wiki/index.php?title=%E9%A6%96%E9%A1%B5>`_

- application_api

  This django application is the API for wechat application account.

`[Application-Interface] <https://mp.weixin.qq.com/debug/wxadoc/dev/index.html>`_

==========
How to use
==========

Install django application django-wechat-api::

    pip install django-wechat-api

Put your configuration in your django project in settings.py::

    INSTALLED_APPS = (
    ...
    'wechat_api',
    'enterprise_api',
    'application_api'
    )

    MYSQL_DB = 'wechat'
    MYSQL_USER = 'django'
    MYSQL_PASS = '******'
    MYSQL_HOST = 'localhost'
    MYSQL_PORT = '3306'

    # For subscribe and service account.
    WECHAT_TOKEN = u'your_token'
    WECHAT_APP_ID = u'your_app_id'
    WECHAT_APP_SECRET = u'your_app_secret'

====
Test
====

Create a django project "wechat" to test.

Deploy this project on Sina SAE platform for test.

---
SAE
---

SAE is sina cloud platform.

site-packages is the third party libraries for SAE.

config.yaml is for SAE.

index.wsgi is for SAE.

wechat.sql is for SAE Mysql.

`[Sina-SAE] <http://www.sinacloud.com/doc/sae/python/index.html>`_

------------------------
Wechat Official Accounts
------------------------

XXXZZZZ is the test Wechat Official Subscribe Account.

.. figure:: https://github.com/crazy-canux/django-wechat-api/blob/master/data/images/xxxzzzz.jpg
   :alt: pic

Canux is the test Wechat Official Enterprise Account.

====
TODO
====

1. Create menu.

=============
Documentation
=============

`[Documentation] <http://django-wechat-api.readthedocs.io/en/latest/>`_

============
Contribution
============

`[Contribution] <https://github.com/crazy-canux/django-wechat-api/blob/master/CONTRIBUTING.rst>`_

=======
Authors
=======

`[Authors] <https://github.com/crazy-canux/django-wechat-api/blob/master/AUTHORS.rst>`_

=======
License
=======

`[License] <https://github.com/crazy-canux/django-wechat-api/blob/master/LICENSE>`_
