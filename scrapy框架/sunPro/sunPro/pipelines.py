# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv

class SunproPipeline(object):
    def open_spider(self, spider):
        print("开始爬虫")
        self.fp = open("./sun.txt", "w", encoding="utf-8")
    def close_spider(self, spider):
        print("结束爬虫")
        self.fp.close()
    def process_item(self, item, spider):
        if item.__class__.__name__ == 'SunproItem':
            print(item['title'])
        if item.__class__.__name__ == 'DetailItem':
            print(item['content'])
        return item

