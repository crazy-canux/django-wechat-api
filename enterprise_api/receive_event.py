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
        wechat用户发送的event类型。

         8.1 event - subscribe
         <xml>
         <ToUserName><![CDATA[toUser]]></ToUserName>
         <FromUserName><![CDATA[UserID]]></FromUserName>
         <CreateTime>1348831860</CreateTime>
         <MsgType><![CDATA[event]]></MsgType>
         <Event><![CDATA[subscribe]]></Event>
         <AgentID>1</AgentID>
         </xml>

         8.2 event - unsubscribe
         <xml>
         <ToUserName><![CDATA[toUser]]></ToUserName>
         <FromUserName><![CDATA[UserID]]></FromUserName>
         <CreateTime>1348831860</CreateTime>
         <MsgType><![CDATA[event]]></MsgType>
         <Event><![CDATA[unsubscribe]]></Event>
         <AgentID>1</AgentID>
         </xml>

         8.3 event - LOCATION
         <xml>
         <ToUserName><![CDATA[toUser]]></ToUserName>
         <FromUserName><![CDATA[FromUser]]></FromUserName>
         <CreateTime>123456789</CreateTime>
         <MsgType><![CDATA[event]]></MsgType>
         <Event><![CDATA[LOCATION]]></Event>
         <Latitude>23.104105</Latitude>
         <Longitude>113.320107</Longitude>
         <Precision>65.000000</Precision>
         <AgentID>1</AgentID>
         </xml>

         8.4 event - CLICK 点击菜单拉取消息时的事件推送
         <xml>
         <ToUserName><![CDATA[toUser]]></ToUserName>
         <FromUserName><![CDATA[FromUser]]></FromUserName>
         <CreateTime>123456789</CreateTime>
         <MsgType><![CDATA[event]]></MsgType>
         <Event><![CDATA[click]]></Event>
         <EventKey><![CDATA[EVENTKEY]]></EventKey>
         <AgentID>1</AgentID>
         </xml>

         8.5 event - VIEW 点击菜单跳转链接时的事件推送
         <xml>
         <ToUserName><![CDATA[toUser]]></ToUserName>
         <FromUserName><![CDATA[FromUser]]></FromUserName>
         <CreateTime>123456789</CreateTime>
         <MsgType><![CDATA[event]]></MsgType>
         <Event><![CDATA[view]]></Event>
         <EventKey><![CDATA[www.qq.com]]></EventKey>
         <AgentID>1</AgentID>
         </xml>

         8.6 event - scancode_push 扫码推事件的事件推送
         <xml><ToUserName><![CDATA[toUser]]></ToUserName>
         <FromUserName><![CDATA[FromUser]]></FromUserName>
         <CreateTime>1408090502</CreateTime>
         <MsgType><![CDATA[event]]></MsgType>
         <Event><![CDATA[scancode_push]]></Event>
         <EventKey><![CDATA[6]]></EventKey>
         <ScanCodeInfo><ScanType><![CDATA[qrcode]]></ScanType>
         <ScanResult><![CDATA[1]]></ScanResult>
         </ScanCodeInfo>
         <AgentID>1</AgentID>
         </xml>

         8.7 event - scancode_waitmsg 扫码推事件且弹出“消息接收中”提示框的事件推送
         <xml><ToUserName><![CDATA[toUser]]></ToUserName>
         <FromUserName><![CDATA[FromUser]]></FromUserName>
         <CreateTime>1408090606</CreateTime>
         <MsgType><![CDATA[event]]></MsgType>
         <Event><![CDATA[scancode_waitmsg]]></Event>
         <EventKey><![CDATA[6]]></EventKey>
         <ScanCodeInfo><ScanType><![CDATA[qrcode]]></ScanType>
         <ScanResult><![CDATA[2]]></ScanResult>
         </ScanCodeInfo>
         <AgentID>1</AgentID>
         </xml>

         8.8 event - pic_sysphoto 弹出系统拍照发图的事件推送
         <xml><ToUserName><![CDATA[toUser]]></ToUserName>
         <FromUserName><![CDATA[FromUser]]></FromUserName>
         <CreateTime>1408090651</CreateTime>
         <MsgType><![CDATA[event]]></MsgType>
         <Event><![CDATA[pic_sysphoto]]></Event>
         <EventKey><![CDATA[6]]></EventKey>
         <SendPicsInfo><Count>1</Count>
         <PicList><item><PicMd5Sum><![CDATA[1b5f7c23b5bf75682a53e7b6d163e185]]></PicMd5Sum>
         </item>
         </PicList>
         </SendPicsInfo>
         <AgentID>1</AgentID>
         </xml>

         8.9 event - pic_photo_or_album 弹出拍照或者相册发图的事件推送
         <xml><ToUserName><![CDATA[toUser]]></ToUserName>
         <FromUserName><![CDATA[FromUser]]></FromUserName>
         <CreateTime>1408090816</CreateTime>
         <MsgType><![CDATA[event]]></MsgType>
         <Event><![CDATA[pic_photo_or_album]]></Event>
         <EventKey><![CDATA[6]]></EventKey>
         <SendPicsInfo><Count>1</Count>
         <PicList><item><PicMd5Sum><![CDATA[5a75aaca956d97be686719218f275c6b]]></PicMd5Sum>
         </item>
         </PicList>
         </SendPicsInfo>
         <AgentID>1</AgentID>
         </xml>

         8.10 event - pic_weixin 弹出微信相册发图器的事件推送
         <xml><ToUserName><![CDATA[toUser]]></ToUserName>
         <FromUserName><![CDATA[FromUser]]></FromUserName>
         <CreateTime>1408090816</CreateTime>
         <MsgType><![CDATA[event]]></MsgType>
         <Event><![CDATA[pic_weixin]]></Event>
         <EventKey><![CDATA[6]]></EventKey>
         <SendPicsInfo><Count>1</Count>
         <PicList><item><PicMd5Sum><![CDATA[5a75aaca956d97be686719218f275c6b]]></PicMd5Sum>
         </item>
         </PicList>
         </SendPicsInfo>
         <AgentID>1</AgentID>
         </xml>

         8.11 event - location_select 弹出地理位置选择器的事件推送
         <xml><ToUserName><![CDATA[toUser]]></ToUserName>
         <FromUserName><![CDATA[FromUser]]></FromUserName>
         <CreateTime>1408091189</CreateTime>
         <MsgType><![CDATA[event]]></MsgType>
         <Event><![CDATA[location_select]]></Event>
         <EventKey><![CDATA[6]]></EventKey>
         <SendLocationInfo><Location_X><![CDATA[23]]></Location_X>
         <Location_Y><![CDATA[113]]></Location_Y>
         <Scale><![CDATA[15]]></Scale>
         <Label><![CDATA[ 广州市海珠区客村艺苑路 106号]]></Label>
         <Poiname><![CDATA[]]></Poiname>
         </SendLocationInfo>
         <AgentID>1</AgentID>
         </xml>

         8.12 event - enter_agent 成员进入应用的事件推送
         <xml><ToUserName><![CDATA[toUser]]></ToUserName>
         <FromUserName><![CDATA[FromUser]]></FromUserName>
         <CreateTime>1408091189</CreateTime>
         <MsgType><![CDATA[event]]></MsgType>
         <Event><![CDATA[enter_agent]]></Event>
         <EventKey><![CDATA[]]></EventKey>
         <AgentID>1</AgentID>
         </xml>

         8.13 event - batch_job_result 异步任务完成事件推送
         <xml><ToUserName><![CDATA[wx28dbb14e37208abe]]></ToUserName>
         <FromUserName><![CDATA[FromUser]]></FromUserName>
         <CreateTime>1425284517</CreateTime>
         <MsgType><![CDATA[event]]></MsgType>
         <Event><![CDATA[batch_job_result]]></Event>
         <BatchJob><JobId><![CDATA[S0MrnndvRG5fadSlLwiBqiDDbM143UqTmKP3152FZk4]]></JobId>
         <JobType><![CDATA[sync_user]]></JobType>
         <ErrCode>0</ErrCode>
         <ErrMsg><![CDATA[ok]]></ErrMsg>
         </BatchJob>
         </xml>
"""
