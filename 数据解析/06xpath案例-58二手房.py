import requests
from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
}
url = "https://bj.58.com/ershoufang/"
page_text = requests.get(url=url, headers=headers).text
tree = etree.HTML(page_text)
li_list = tree.xpath("//ul[@class='house-list-wrap']/li")
f = open("58.txt", "w", encoding="utf-8")
for li in li_list:
    title = li.xpath("./div[2]/h2/a/text()")[0]
    print(title)
    f.write(title + '\n')