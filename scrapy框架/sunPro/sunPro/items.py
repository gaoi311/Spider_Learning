# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SunproItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    new_id = scrapy.Field()

class DetailItem(scrapy.Item):
    content = scrapy.Field()