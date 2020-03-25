import requests

#UA伪装
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
}
url = "https://www.sogou.com/web"
#处理url携带的参数: 封装到字典中
kw = input("enter a word:")
param = {
    'query': kw,
}
#对指定的url发送的请求时携带请求的
response = requests.get(url=url, params=param, headers=headers)
text = response.text
filename = kw + ".html"
with open(filename, "w", encoding="utf-8") as f:
    f.write(text)

print(filename, "保存成功!!!")
