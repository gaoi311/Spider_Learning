from selenium import webdriver
from lxml import etree
bro = webdriver.Chrome(executable_path=r'E:\PythonFiles\Project\爬虫\selenium模块应用\chromedriver.exe')

bro.get('http://125.35.6.84:81/xk/')

page_text = bro.page_source

tree = etree.HTML(page_text)
li_list = tree.xpath('//ul[@id="gzlist"]/li')
for li in li_list:
    name = li.xpath('./dl/@title')[0]
    print(name)