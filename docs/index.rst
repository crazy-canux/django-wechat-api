.. django-wechat-api documentation master file, created by
   sphinx-quickstart on Tue Nov  8 22:04:13 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

django-wechat-api
=================

This project is the python/django API for wechat official account development.

wechat is the django project used for test django applications.

wechat_api is a django application for wechat subscribe and service account.

enterprise_api is a django application for wechat enterprise account.

application_api is a django application for wechat application account.

How to install
==============

Install the django application::

    $pip install django-wechat-api

Create a django project for example named wechat.

And put this configuration in the project wechat::

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

How to use
==========

Register the wechat official account for test.

And deploy the code on BAE, SAE or BAE.

The User Guid
=============

.. toctree::
   :maxdepth: 2

   wechat
   wechat_api
   enterprise_api
   application_api



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

