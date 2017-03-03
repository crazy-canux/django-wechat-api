.. _wechat_api:

wechat_api
==========

This django application is the API for wechat subscribe and service account.

微信订阅号和服务号的接口是一样的．



已实现的功能：

- 接收用户发送的文本消息，通过图灵机器人回复
- 接收用户发送的图片消息，通过微软的how-old回复年龄和性别



待实现的功能：

- 接收用户发送的其它类型的消息的回复
- 接收用户发送的事件类型的消息并回复
- 定制菜单



不实现的功能：

- 主动给用户推送消息
- 其它高级功能



Release:

- receive message format
- response message format
- response text message with tuling123.com
- response image message with how-old.net

Todo:

- response message like voice, video/shortvideo, location, link
- receive event format
- response event
- customise menu
