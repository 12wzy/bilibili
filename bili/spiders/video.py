import scrapy
import logging
import json
from scrapy.contrib.spiders import CrawlSpider
from ..videoItems import videoItem
from ..videoTagItems import videoTagItem
HTTPS = "https:"
HOST = "https://api.bilibili.com"


class biliSpider(CrawlSpider):
    name = "biliSpider"
    start_urls = []
    tags_url = "https://api.bilibili.com/x/tag/archive/tags?aid={}"
    for i in range(50, 100):
        start_urls.append("{}/x/web-interface/view?aid={}".format(HOST, str(i + 1)))

    def parse(self, response):
        self.log('Hi, this is an item page! %s' % response.url, level=logging.WARNING)

        videoInfo = response.body.decode('utf-8')
        videoInfoJson = json.loads(videoInfo)
        exist = int(videoInfoJson['code'])
        if exist == 0:
            video = videoItem()
            video["videoId"] = videoInfoJson['data']['aid']
            video["videoLabelId"] = videoInfoJson['data']['tid']
            video["videoLabelName"] = videoInfoJson['data']['tname']
            video["videoTitle"] = videoInfoJson['data']['title']
            video["pubDate"] = videoInfoJson['data']['pubdate']
            video["view"] = videoInfoJson['data']['stat']['view']
            video["danmaku"] = videoInfoJson['data']['stat']['danmaku']
            video["reply"] = videoInfoJson['data']['stat']['reply']
            video["favorite"] = videoInfoJson['data']['stat']['favorite']
            video["coin"] = videoInfoJson['data']['stat']['coin']
            video["share"] = videoInfoJson['data']['stat']['share']
            video["ownerId"] = videoInfoJson['data']['owner']['mid']
            video["ownerName"] = videoInfoJson['data']['owner']['name']
            yield video
            yield scrapy.Request(self.tags_url.format(video["videoId"]), callback=self.parse_tags)

    def parse_tags(self, response):

        tag_info = response.body.decode('utf-8')
        tag_info_json = json.loads(tag_info)
        tags = tag_info_json['data']
        video_id = response.url.split('?aid=')[1]
        if tags is not None:
            self.log('Tag is not none and the number is %d' % len(tags), level=logging.INFO)
            tag_item = videoTagItem()
            tag_item['videoId'] = int(video_id)
            for tag in tags:
                tag_item['tagId'] = tag['tag_id']
                tag_item['tagName'] = tag['tag_name']
                self.log('tag item: %s' % str(tag_item), level=logging.INFO)
                yield tag_item

