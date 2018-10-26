# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class videoTagItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    videoId = scrapy.Field()                # av Number
    tagId = scrapy.Field()
    tagName = scrapy.Field()
    pass
