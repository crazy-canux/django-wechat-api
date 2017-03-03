.. _enterprise_api:

enterprise_api
==============

This django application is the API for wechat enterprise account.

微信企业号有两种调用模式：

- 主动调用(可用于主动给用户发送消息)
- 回调模式(类似于订阅号和服务号的被动响应用户发送的消息和事件)



已实现的功能：

- 回调模式接收用户发送的文本消息，用图灵机器人回复．
- 回调模式接收用户发送的图片消息，用微软的how-old回复性别和年龄．



待实现的功能：

- 回调模式接收用户发送的其它类型消息并回复．
- 回调模式接收用户发送的事件并回复．
- 主动调用模式给用户推送消息．



暂不实现的功能：

- 认证接口
- 资源接口
- 其它能力接口的高级功能



Release:

- receive message format
- response message format
- send message format



Todo:

- response text message with tuling123.com
- response image message with how-old.net
- send message
- receive event format
- response event message

