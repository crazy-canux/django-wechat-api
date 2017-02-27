.. _wechat:

wechat
======

wechat is a django project created for test wechat API applications.



Include:

`[Wechat subscribe&service Interface] <https://mp.weixin.qq.com/wiki/home/>`_

`[Enterprise Interface] <http://qydev.weixin.qq.com/wiki/index.php?title=%E9%A6%96%E9%A1%B5>`_

`[Application Interface] <https://mp.weixin.qq.com/debug/wxadoc/dev/index.html>`_



And some other functions:

- Use http://how-old.net to anylyze the age of a picture.
- Use http://www.tuling123.com to auto response message.



How to use
==========

0. Register your wechat official account.

1. Create django project wechat::

    $django-admin startproject wechat

2. Install this django application::

    $pip install django-wechat-api

3. Configuration the django project in settings.py::

    INSTALLED_APPS = (
    ...
    # Just choose which you need
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

4. Deploy your project on SAE or BAE to test.
