import requests

from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
}

url = "http://www.shicimingju.com/book/sanguoyanyi.html"
page_text = requests.get(url, headers).text

soup = BeautifulSoup(page_text, "lxml")
li_list = soup.select('.book-mulu > ul > li')
f = open("sanguo.txt", "w", encoding="utf-8")
for li in li_list:
    title = li.a.string
    detail_url = "http://www.shicimingju.com" + li.a['href']
    detail_page = requests.get(detail_url, headers=headers).text
    detail = BeautifulSoup(detail_page, "lxml")
    div_tag = detail.find('div', class_='chapter_content')
    content = div_tag.text
    f.write(title + ":" + content)

f.close()