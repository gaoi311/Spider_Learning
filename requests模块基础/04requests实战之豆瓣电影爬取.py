import json

import requests


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
}
url = "https://movie.douban.com/j/chart/top_list"
params = {
    "type": 24,
    "interval_id": "100:90",
    "action": "",
    "start": "0",
    "limit": "20"
}

response = requests.get(url=url, params=params, headers=headers)
list_data = response.json()

fp = open("douban.json", "w", encoding="utf-8")
json.dump(list_data, fp, ensure_ascii=False)
print("over!!!")