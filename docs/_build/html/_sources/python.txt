.. _python:

python开发微信公众号
====================

1. 注册微信公众号(订阅号/服务号，企业号, 小程序)
2. 在微信公众平台（开发->基本配置）修改服务器配置，URL添加你的代码的URL，Token添加你代码中的Token。
3. 用git管理代码提交到URL，或者部署到云服务器。

微信开发文档：

`[wechat docs] <https://mp.weixin.qq.com/>`_

流程::

    wechat user <=> send/receive message <=> wechat server <=> POST XML message <=> your server

云平台部署django项目
====================

`[SAE] <http://www.sinacloud.com/doc/sae/python/index.html>`_

`[BAE] <https://cloud.baidu.com/doc/BAE/QuickGuide.html>`_

SAE添加第三方依赖：

`[SAE vendor] <http://www.sinacloud.com/doc/sae/python/tools.html#tian-jia-di-san-fang-yi-lai-bao>`_

BAE添加第三方依赖::

    $vim requirements.txt
    django==1.8.2
    ...

使用mysql：

`[SAE mysql] <http://www.sinacloud.com/doc/sae/python/mysql.html#api-shi-yong-shou-ce>`_

SAE平台需要config.yaml和index.wsgi两个文件.

SAE的入口就是index.wsgi文件中名叫application的可调用对象。

BAE平台需要app.conf,favicon.ico和index.py三个文件。

BAE的入口就是index.py文件中名叫application的可调用对象。

创建django项目wechat
====================

app.conf或conf.yaml添加配置文件。

index.wsgi或index.py添加云平台入口。

wechat/settings.py添加mysql数据库信息。

在GAE/BAE/SAE设置mysql，在项目添加mysql的参数。

用migrate同步本地数据库后，用下面命令导出本地数据为sql文件::

    $ python manage.py migrate
    $ mysqldump -u <username> -p <databasename> > <filename>.sql

在GAE/BAE/SAE上传sql文件把数据同步到GAE/BAE/SAE的mysql。

创建django的应用django-wechat-api
=================================

在wechat/settings.py中添加应用。

在wechat/urls.py中添加应用的url。

在django-wechat-api/views.py添加微信接口。

修改wechat公众平台配置
======================

配置::

    SAE_URL: http://<project>.applinzi.com/wechat/
    BAE_URL: http://<project>.duapp.com/wechat/
    TOKEN: yourtoken

django开发的wechat接口开源项目
==============================

源码参考:

`[github] <https://github.com/crazy-canux/django-wechat-api>`_

