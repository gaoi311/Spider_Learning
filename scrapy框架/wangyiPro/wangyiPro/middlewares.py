# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from time import sleep
from scrapy.http import HtmlResponse

class WangyiproDownloaderMiddleware(object):
    def process_request(self, request, spider):
    
        return None

    def process_response(self, request, response, spider):
        bro = spider.bro
        if request.url in spider.models_urls:
            bro.get(request.url)
            page_text = bro.page_source
            new = HtmlResponse(url=request.url, body=page_text, encoding='utf-8', request=request)
            return new
        return response

    def process_exception(self, request, exception, spider):
      
        pass
