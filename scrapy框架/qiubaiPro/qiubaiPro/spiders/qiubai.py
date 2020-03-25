# -*- coding: utf-8 -*-
import scrapy
from qiubaiPro.items import QiubaiproItem

class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    # allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.funnyba.com/']

    def parse(self, response):
        li_list = response.xpath('//*[@id="content"]/div/div[2]/div/ul/li')
        # print(li_list)
        # all_data = []
        for li in li_list:
            author = li.xpath('./div/div/a/span/text()').extract_first()
            content = li.xpath('./div/a/text()').extract_first()

            item = QiubaiproItem()
            item['author'] = author
            item['content'] = content

            yield item