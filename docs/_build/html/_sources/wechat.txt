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
----------

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

    # SAE/BAE:True means on server, False means on local.
    DEPLOY = 'SERVER_SOFTWARE' in os.environ

    # For SAE
    if DEPLOY:
        import sae.const
        MYSQL_DB = sae.const.MYSQL_DB
        MYSQL_USER = sae.const.MYSQL_USER
        MYSQL_PASS = sae.const.MYSQL_PASS
        MYSQL_HOST = sae.const.MYSQL_HOST
        MYSQL_PORT = sae.const.MYSQL_PORT
    # For BAE
    #if DEPLOY:
    #    MYSQL_DB = '******'
    #    MYSQL_USER = '******'
    #    MYSQL_PASS = '******'
    #    MYSQL_HOST = 'sqld.duapp.com'
    #    MYSQL_PORT = '4050'
    # For Local
    else:
         MYSQL_DB = 'wechat'
         MYSQL_USER = '******'
         MYSQL_PASS = '******'
         MYSQL_HOST = 'localhost'
         MYSQL_PORT = '3306'

    # For wechat subscribe and service account.
    WECHAT_TOKEN = u'your_token'
    WECHAT_APP_ID = u'your_app_id'
    WECHAT_APP_SECRET = u'your_app_secret'

    # For wechat enterprise account.
    CORPID = "your_corp_id"
    TOKEN = "your_token"
    ENCODINGAESKEY = "your_encoding_aeskey"
    SECRET = "your_secret"
    AGENTID = 0
    SAFE = 0

4. Configuration the django project in urls.py::

    urlpatterns = [
        url(r'^wechat/', include('wechat_api.urls', namespace='wechat_api')),
        url(r'^enterprise/', include('enterprise_api.urls', namespace='enterprise_api')),
    ]

5. Deploy your project on SAE or BAE to test::

    # Export data from local mysql and import to SAE/BAE
    $mysqldump -u <username> -p <databasename> > <filename>.sql

6. Register your wechat official account and fill in your SAE/BAE url and your tocken::

    URL(SAE): http://<project>.applinzi.com/<wechat/enterprise>/
    URL(BAE): http://<project>.duapp.com/<wechat/enterprise>/
    TOKEN: yourtoken
