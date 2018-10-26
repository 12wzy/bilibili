# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class videoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    videoId = scrapy.Field()                # av Number
    videoLabelId = scrapy.Field()
    videoLabelName = scrapy.Field()
    videoTitle = scrapy.Field()
    pubDate = scrapy.Field()                # publish date
    view = scrapy.Field()
    danmaku = scrapy.Field()
    reply = scrapy.Field()
    favorite = scrapy.Field()
    coin = scrapy.Field()
    share = scrapy.Field()
    ownerId = scrapy.Field()
    ownerName = scrapy.Field()
    pass
