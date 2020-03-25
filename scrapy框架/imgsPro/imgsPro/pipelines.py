# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# class ImgsproPipeline(object):
#     def process_item(self, item, spider):
#         return item

from scrapy.pipelines.images import ImagesPipeline
import scrapy
class ImgsPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        yield scrapy.Request(item['src'])

    def file_path(self, request, response=None, info=None):
        imgname = request.url.split('/')[-1]
        return imgname

    def item_completed(self, results, item, info):
        return item
