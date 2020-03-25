import json

import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
}
url = "https://fanyi.baidu.com/sug"
kw = input("enter a word")
data = {
    "kw": kw
}

text_dict = requests.post(url=url, data=data, headers=headers).json()
filename = kw + ".json"
f = open(filename, "w", encoding="utf-8")
json.dump(text_dict, f, ensure_ascii=False)
print(text_dict)