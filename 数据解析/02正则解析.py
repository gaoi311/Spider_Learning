import re

import requests

import os

if not os.path.exists("糗图"):
    os.mkdir("糗图")
url = "http://www.funnyba.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
}

page_text = requests.get(url=url, headers=headers).text
ex = '<div class="recmd-detail clearfix">.*?src="(.*?)" alt=.*?/>'
img_list = re.findall(ex, page_text, re.S)
for src in img_list:
    src = src.split('?')[0]
    img = requests.get(url=src, headers=headers).content
    img_name = src.split('/')[-1]
    imgpath = "糗图/" + img_name
    with open(imgpath, "wb") as f:
        f.write(img)
        print(img_name, "下载成功!")