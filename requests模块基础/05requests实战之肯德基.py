import json

import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
}
url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword"

data = {
    "cname": "",
    "pid": "",
    "keyword": "合肥",
    "pageIndex": "1",
    "pageSize": "10"
}
response = requests.post(url=url, data=data, headers=headers)
text = response.text

f = open("肯德基合肥.json", "w", encoding="utf-8")
json.dump(text, f, ensure_ascii=False)
print("over!!")