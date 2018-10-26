# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
import time
from .videoItems import videoItem
from .videoTagItems import videoTagItem
import logging
import os
from bili.util.database.mysql import MySQL

class TutorialPipeline(object):

    def __init__(self):
        self.mysql = MySQL()
        self.connection = self.mysql.createConnection()

    def process_item(self, item, spider):
        sql = ""
        try:
            if isinstance(item, videoItem):
                sql = self.mysql.insert2video(item, self.connection)
            elif isinstance(item, videoTagItem):
                sql = self.mysql.insert2tag(item, self.connection)
            logging.info("[EXCUTE SQL] {sql}".format(sql=sql))
        except Exception as e:
            with open('{}/bilibiliSpider/log/exception_log_{}.txt'.format(os.getcwd(), time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime(time.time()))), 'w') as f:
                f.write("=============================================\n")
                f.write(sql+'\n')
                f.write(str(e)+'\n')

        return item

    def spider_closed(self, spider):

        self.mysql.closeConnection(self.connection)