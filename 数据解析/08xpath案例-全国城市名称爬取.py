import requests

from lxml import etree

# url = "https://www.aqistudy.cn/historydata/"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
# }
#
# page_text = requests.get(url, headers).text
# tree = etree.HTML(page_text)
# li_list = tree.xpath("//div[@class='bottom']/ul/li")
# all_city_names = []
# for li in li_list:
#     hot_city_name = li.xpath("./a/text()")[0]
#     all_city_names.append(hot_city_name)
#
# city_names = tree.xpath("//div[@class='bottom']/ul/div[2]/li")
# for li in city_names:
#     city_name = li.xpath("./a/text()")[0]
#     all_city_names.append(city_name)
#
# print(all_city_names, len(all_city_names))

url = "https://www.aqistudy.cn/historydata/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
}

page_text = requests.get(url, headers).text
tree = etree.HTML(page_text)
li_list = tree.xpath("//div[@class='bottom']/ul/li/a | //div[@class='bottom']/ul/div[2]/li/a")
city_names = []
for li in li_list:
    city_name = li.xpath("./text()")[0]
    city_names.append(city_name)
print(city_names, len(city_names))