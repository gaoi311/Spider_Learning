import requests
from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
}
url = "http://sc.chinaz.com/jianli/index_{}.html"

f = open("简历.txt", "w", encoding="utf-8")
for page in range(2, 10):
    page_url = url.format(page)
    page_text = requests.get(page_url).text
    tree = etree.HTML(page_text)
    jianli_div_list = tree.xpath("//div[@id='main']/div/div")
    print(jianli_div_list)
    for jianli_div in jianli_div_list:
        jianli_title = jianli_div.xpath("./p/a/text()")[0]
        jianli_title = jianli_title.encode('iso-8859-1').decode("utf-8")
        jianli_src = jianli_div.xpath("./p/a/@href")[0]
        jianli = jianli_title + "--->" + jianli_src
        f.write(jianli + "\n")
        print(jianli_title + "打印完成!!!")

f.close()