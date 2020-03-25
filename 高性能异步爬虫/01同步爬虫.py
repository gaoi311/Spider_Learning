import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
}

urls = {
    "http://xmdx.sc.chinaz.net/Files/Download/jianLi/201904/jianli10231.rar",
    "http://xmdx.sc.chinaz.net/Files/Download/jianLi/201904/jianli10229.rar",
    "http://xmdx.sc.chinaz.net/Files/Download/jianLi/201904/jianli10231.rar",
}

def get_content(url):
    print("正在爬取:", url)
    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        return response.content

def parse_content(content):
    print("响应数据的长度为:", len(content))

for url in urls:
    content = get_content(url)
    parse_content(content)