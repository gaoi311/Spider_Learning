import requests

from lxml import etree
import os

if not os.path.exists("美女"):
    os.mkdir("美女")
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
}
url = "http://pic.netbian.com/4kmeinv"
response = requests.get(url, headers)
# response.encoding = "utf-8"
page_text = response.text

tree = etree.HTML(page_text)
li_list = tree.xpath("//div[@class='slist']/ul/li")
for li in li_list:
    img_src = "http://pic.netbian.com" + li.xpath("./a/img/@src")[0]
    img_name = li.xpath("./a/img/@alt")[0] + ".jpg"
    img_name = img_name.encode('iso-8859-1').decode("gbk")
    img_data = requests.get(img_src).content
    filename = "美女/" + img_name
    with open(filename, "wb") as f:
        f.write(img_data)
        print(img_name + "over!!!")
