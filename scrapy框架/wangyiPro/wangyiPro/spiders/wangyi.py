# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from wangyiPro.items import WangyiproItem
class WangyiSpider(scrapy.Spider):
    name = 'wangyi'
    # allowed_domains = ['news.163.com/']
    start_urls = ['http://news.163.com/']
    models_urls = []
    # all_data = []
    def __init__(self):
        self.bro = webdriver.Chrome(executable_path=r'E:\PythonFiles\Project\爬虫\scrapy框架\wangyiPro\chromedriver.exe')
    def parse(self, response):
        li_list = response.xpath('//*[@id="index2016_wrap"]/div[1]/div[2]/div[2]/div[2]/div[2]/div/ul/li')
        alist = [4]
        for index in alist:
            mo = li_list[index].xpath('./a/@href').extract_first()
            self.models_urls.append(mo)
        for url in self.models_urls:
            yield scrapy.Request(url=url, callback=self.parse_model)
            print(url)

    def parse_model(self, response):
        div_list = response.xpath('/html/body/div/div[3]/div[4]/div[1]/div/div/ul/li/div/div')
        for div in div_list:
            new_detail_url = div.xpath('./div/div[1]/h3/a/@href').extract_first()
            title = div.xpath('./div/div[1]/h3/a/text()').extract_first()
            item = WangyiproItem()
            item['title'] = title
            yield scrapy.Request(url=new_detail_url, callback=self.parse_detail, meta={'item': item})

    def parse_detail(self, response):
        content = response.xpath('//*[@id="endText"]//text()').extract()
        content = ''.join(content)
        item = response.meta['item']
        item['content'] = content
        yield item

    def closed(self, spider):
        self.bro.quit()