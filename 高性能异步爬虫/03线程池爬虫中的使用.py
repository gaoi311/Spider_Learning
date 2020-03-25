import requests
import re
from lxml import etree
from multiprocessing.dummy import Pool
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
}

url = "https://www.pearvideo.com/category_5"
page_text = requests.get(url=url, headers=headers).text

tree = etree.HTML(page_text)
li_list = tree.xpath('//*[@id="listvideoListUl"]/li')
urls = []
for li in li_list:
    url = "https://www.pearvideo.com/" + li.xpath('./div/a/@href')[0]
    name = li.xpath('./div/a/div[2]/text()')[0]
    # print(name, url)
    detail = requests.get(url, headers=headers).text
    tree = etree.HTML(detail)
    ex = 'srcUrl="(.*?)",vdoUrl'
    video_url = re.findall(ex, detail)[0]
    # video_url = tree.xpath('/html/body/div[2]/div[1]/div[1]/div[1]/div[1]/div/video/@src')
    dic = {
        'name': name,
        'url': video_url
    }
    urls.append(dic)

def get_data(dic):
    url = dic['url']
    name = dic['name'] + ".mp4"
    print(name, "正在下载！！！")
    date = requests.get(url=url, headers=headers).content
    with open(name, "wb") as f:
        f.write(date)
        print(name, "下载完成！！！")

pool = Pool(4)
pool.map(get_data, urls)

pool.close()
pool.join()