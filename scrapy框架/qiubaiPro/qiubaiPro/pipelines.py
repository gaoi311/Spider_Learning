# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class QiubaiproPipeline(object):
    def open_spider(self, spider):
        print("开始爬虫")
        self.fp = open("./qiubai.txt", "w", encoding='utf-8')
    def process_item(self, item, spider):
        author = item['author']
        content = item['content']

        self.fp.write(author + "：" + content + '\n')
        return item

    def close_spider(self, spider):
        print("结束爬虫")
        self.fp.close()
    
class mysqlpipeline(object):

    # def __init__(self):
    #     self.conn = None
    #     self.cursor = None
    def open_spider(self, spider):
        self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root', db='db1')
    def process_item(self, item, spider):
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute('insert into qiubai (author, content) values ("%s", "%s")' % (item['author'], item['content']))
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()

        return item
    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()