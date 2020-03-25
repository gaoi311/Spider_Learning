# -*- coding: utf-8 -*-
import scrapy


class FirstSpider(scrapy.Spider):
    # 爬虫文件的名称: 就是爬虫源文件的一个唯一标志
    name = 'first'
    # 允许的域名, 用来限定start_urls列表中哪些urk可以进行发送
    # allowed_domains = ['www.baidu.com']
    # 起始的url列表, 该列表中存放的url会被scrapy自动请求发送
    start_urls = ['https://www.baidu.com/', 'https://www.sogou.com/']

    # 用做于数据解析
    def parse(self, response):
        print(response)
