#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Send message from django server to wechat server.

Copyright (C) 2016 Canux CHENG.
All rights reserved.
Name: send_message.py
Author: Canux CHENG canuxcheng@gmail.com
Version: V1.0.0.0
Time: Tue 11 Oct 2016 12:22:40 AM EDT

Details:
    check the wechat doc, just support 6 kinds of message types.
"""


class BasicSend(object):

    """Basic class for send message.

    All message django server send to wechat server must have this four arguments.
    Wechat Just support send [text, image, voice, video, music, news].
    """

    def __init__(self):
        """Init some definition for message types."""
        # Send/response message types to wechat user.
        RESP_MESSAGE_TYPE_TEXT = u'text'
        RESP_MESSAGE_TYPE_IMAGE = u'image'
        RESP_MESSAGE_TYPE_VOICE = u'voice'
        RESP_MESSAGE_TYPE_VIDEO = u'video'
        RESP_MESSAGE_TYPE_MUSIC = u'music'
        RESP_MESSAGE_TYPE_NEWS = u'news'
        MESSAGE_TYPE = [u'Text', u'Image', u'Voice', u'Video', u'Music', u'News']

        # All send message have this arguments.
        self.to_user_name = u''
        self.from_user_name = u''
        self.create_time = u''
        self.msg_type = u''

    def get_to_user_name(self):
        return self.to_user_name

    def set_to_user_name(self, to_user_name):
        self.to_user_name = to_user_name

    def get_from_user_name(self):
        return self.from_user_name

    def set_from_user_name(self, from_user_name):
        self.from_user_name = from_user_name

    def get_create_time(self):
        return self.create_time

    def set_create_time(self, create_time):
        self.create_time = create_time

    def get_msg_type(self):
        return self.msg_type

    def set_msg_type(self, msg_type):
        self.msg_type = msg_type


class Text(object):

    """Basic text object class."""

    def __init__(self):
        self.content = u''

    def get_content(self):
        return self.content

    def set_content(self, content):
        self.content = content


class SendText(BasicSend):

    """Reply text message."""

    def __init__(self):
        super(SendText, self).__init__()
        self.text_object = Text()

    def get_text(self):
        return self.text_object

    def set_text(self, text_object):
        self.text_object = text_object


class Image(object):

    """Basic Image object class."""

    def __init__(self):
        self.media_id = u''

    def get_media_id(self):
        return self.media_id

    def set_media_id(self, media_id):
        self.media_id = media_id


class SendImage(BasicSend):

    """Reply image message."""

    def __init__(self):
        super(SendImage, self).__init__()
        self.image_object = Image()

    def get_image(self):
        return self.image_object

    def set_image(self, image_object):
        self.image_object = image_object


class Voice(object):

    """Basic voice class."""

    def __init__(self):
        self.media_id = u''

    def get_media_id(self):
        return self.media_id

    def set_media_id(self, media_id):
        self.media_id = media_id


class SendVoice(BasicSend):

    """Reply voice message."""

    def __init__(self):
        super(SendVoice, self).__init__()
        self.voice_object = Voice()

    def get_voice(self):
        return self.voice_object

    def set_voice(self, voice_object):
        self.voice_object = voice_object


class Video(object):

    """Basic video class."""

    def __init__(self):
        self.media_id = u''
        self.title = u''
        self.description = u''

    def get_media_id(self):
        return self.media_id

    def set_media_id(self, media_id):
        self.media_id = media_id

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description


class SendVideo(BasicSend):

    """Reply video message."""

    def __init__(self):
        super(SendVideo, self).__init__()
        self.video_object = Video()

    def get_video(self):
        return self.video_object

    def set_video(self, video_object):
        self.video_object = video_object


class Music(object):

    """Basic music class."""

    def __init__(self):
        self.title = u''
        self.description = u''
        self.music_url = u''
        self.hq_music_url = u''
        self.thumb_media_id = u''

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def get_music_url(self):
        return self.music_url

    def set_music_url(self, music_url):
        self.music_url = music_url

    def get_hq_music_url(self):
        return self.hq_music_url

    def set_hq_music_url(self, hq_music_url):
        self.hq_music_url = hq_music_url

    def get_thumb_media_id(self):
        return self.thumb_media_id

    def set_thumb_media_id(self, thumb_media_id):
        self.thumb_media_id = thumb_media_id


class SendMusic(BasicSend):

    """Reply music message."""

    def __init__(self):
        super(SendMusic, self).__init__()
        self.music_object = Music()

    def get_music(self):
        return self.music_object

    def set_music(self, music_object):
        self.music_object = music_object


class News(object):

    """Basic news object class."""

    def __init__(self):
        self.article_count = u''
        self.articles = u''
        self.title = u''
        self.description = u''
        self.pic_url = u''
        self.url = u''

    def get_article_count(self):
        return self.article_count

    def set_article_count(self, article_count):
        self.article_count = article_count

    def get_articles(self):
        return self.articles

    def set_articles(self, articles):
        self.articles = articles

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def get_pic_url(self):
        return self.pic_url

    def set_pic_url(self, pic_url):
        self.pic_url = pic_url

    def get_url(self):
        return self.url

    def set_url(self, url):
        self.url = url


class SendNews(BasicSend):

    """Send news message."""

    def __init__(self):
        super(SendNews, self).__init__()
        self.news_object = News()

    def get_news(self):
        return self.news_object

    def set_news(self, news_object):
        self.news_object = news_object
