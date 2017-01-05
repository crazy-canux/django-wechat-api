#!/usr/bin/env python
# -*- coding: utf-8 -*-
u"""
Wechat user send event to wechat server and transfer to django server.

Copyright (C) 2016 Canux CHENG.
All rights reserved.
Name: receive_event.py
Author: Canux CHENG canuxcheng@gmail.com
Version: V1.0.0.0
Time: Fri 14 Oct 2016 11:36:50 AM EDT

DESCRIPTION:
    wechat用户通过http的post发送的event类型。

         8.1 event - subscribe
         <xml>
         <ToUserName><![CDATA[toUser]]></ToUserName>
         <FromUserName><![CDATA[FromUser]]></FromUserName>
         <CreateTime>123456789</CreateTime>
         <MsgType><![CDATA[event]]></MsgType>
         <Event><![CDATA[subscribe]]></Event>
         </xml>

         8.2 event - unsubscribe
         <xml>
         <ToUserName><![CDATA[toUser]]></ToUserName>
         <FromUserName><![CDATA[FromUser]]></FromUserName>
         <CreateTime>123456789</CreateTime>
         <MsgType><![CDATA[event]]></MsgType>
         <Event><![CDATA[unsubscribe]]></Event>
         </xml>

         8.3 event - subscribe 用户未关注时扫描带参数二维码事件，用户可以关注公众号，关注后将带场景值扫描事件推送给开发者
         <xml><ToUserName><![CDATA[toUser]]></ToUserName>
         <FromUserName><![CDATA[FromUser]]></FromUserName>
         <CreateTime>123456789</CreateTime>
         <MsgType><![CDATA[event]]></MsgType>
         <Event><![CDATA[subscribe]]></Event>
         <EventKey><![CDATA[qrscene_123123]]></EventKey>
         <Ticket><![CDATA[TICKET]]></Ticket>
         </xml>

         8.4 event - SCAN 用户已关注时扫描带参数二维码事件，将带场景值扫描事件推送给开发者
         <xml>
         <ToUserName><![CDATA[toUser]]></ToUserName>
         <FromUserName><![CDATA[FromUser]]></FromUserName>
         <CreateTime>123456789</CreateTime>
         <MsgType><![CDATA[event]]></MsgType>
         <Event><![CDATA[SCAN]]></Event>
         <EventKey><![CDATA[SCENE_VALUE]]></EventKey>
         <Ticket><![CDATA[TICKET]]></Ticket>
         </xml>

         8.5 event - LOCATION
         <xml>
         <ToUserName><![CDATA[toUser]]></ToUserName>
         <FromUserName><![CDATA[fromUser]]></FromUserName>
         <CreateTime>123456789</CreateTime>
         <MsgType><![CDATA[event]]></MsgType>
         <Event><![CDATA[LOCATION]]></Event>
         <Latitude>23.137466</Latitude>
         <Longitude>113.352425</Longitude>
         <Precision>119.385040</Precision>
         </xml>

         8.6 event - CLICK 点击菜单拉取消息时的事件推送
         <xml>
         <ToUserName><![CDATA[toUser]]></ToUserName>
         <FromUserName><![CDATA[FromUser]]></FromUserName>
         <CreateTime>123456789</CreateTime>
         <MsgType><![CDATA[event]]></MsgType>
         <Event><![CDATA[CLICK]]></Event>
         <EventKey><![CDATA[EVENTKEY]]></EventKey>
         </xml>

         8.7 event - VIEW 点击菜单跳转链接时的事件推送
         <xml>
         <ToUserName><![CDATA[toUser]]></ToUserName>
         <FromUserName><![CDATA[FromUser]]></FromUserName>
         <CreateTime>123456789</CreateTime>
         <MsgType><![CDATA[event]]></MsgType>
         <Event><![CDATA[VIEW]]></Event>
         <EventKey><![CDATA[www.qq.com]]></EventKey>
         </xml>
"""
