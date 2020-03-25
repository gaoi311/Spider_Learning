# -*- coding: utf-8 -*-
import scrapy

from bossPro.items import BossproItem
#####################
# boss反爬，爬取失败 #
#####################

class BossSpider(scrapy.Spider):
    name = 'boss'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.zhipin.com/job_detail/?query=python&city=101220100&industry=&position=']

    url = 'https://www.zhipin.com/c100010000/e_102/?query=python&page=%d'
    page_num = 2
    def parse_detail(self, response):
        item = response['meta']
        job_detail = response.xpath('//*[@id="main"]/div[3]/div/div[2]/div[2]/div[1]/div//text()').extract()
        job_detail = ''.join(job_detail)
        item['job_desc'] = job_detail

        yield item

    def parse(self, response):
        li_list = response.xpath('/html/body/div/div[3]/div/div[2]/ul/li')
        for li in li_list:
            item = BossproItem()
            job_name = li.xpath('.//div[@class="info-primary"]/h3/a/div[1]/text()').extract_first()
            item['job_name'] = job_name
            detial_url = 'https://www.zhipin.com' + li.xpath('.//div[@class="info-primary"]/h3/a/@href').extract_first()
            yield scrapy.Request(url=detial_url, callback=self.parse_detail, meta={'item': item})

        if self.page_num <= 3:
            new_url = format(self.url % self.page_num)
            self.page_num += 1

            yield scrapy.Request(new_url, callback=self.parse)