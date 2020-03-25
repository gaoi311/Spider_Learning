# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from sunPro.items import SunproItem, DetailItem 

class SunSpider(CrawlSpider):
    name = 'sun'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://wz.sun0769.com/political/index/politicsNewest?id=1&page=1']

    # link_detail = LinkExtractor(allow=r'/politics/index?id=\d+')
    rules = (
        Rule(LinkExtractor(allow=r'.+id=\d+&page=\d+'), callback='parse_item', follow=False),
        Rule(LinkExtractor(allow=r'.+id=\d+'), callback='parse_detail', follow=False)
    )
    

    def parse_item(self, response):
        li_list = response.xpath('/html/body/div[2]/div[3]/ul[2]/li')
        for li in li_list:
            new_id = li.xpath('./span/text()').extract_first()
            new_title = li.xpath('./span[3]//text()').extract_first()
            item = SunproItem()
            item['new_id'] = new_id
            item['title'] = new_title
            yield item

    def parse_detail(self, response):
        new_content = response.xpath('/html/body/div[3]/div[2]/div[2]/div[2]/pre/text()').extract()
        new_content = ''.join(new_content)
        item = DetailItem()
        item['content'] = new_content
    
        yield item