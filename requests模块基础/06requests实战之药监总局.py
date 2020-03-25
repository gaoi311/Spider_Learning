import json

import requests

f = open("药监总局.json", "w", encoding="utf-8")
id_list = []
all_data =[]
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
}

url = "http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsList"
for page in range(1, 3):
    page = str(page)
    data = {
        "on": "true",
        "page": page,
        "pageSize": "15",
        "productName": "",
        "conditionType": "1",
        "applyname": "",
        "applysn": ""
    }

    json_ids = requests.post(url=url, data=data, headers=headers).json()
    for dic in json_ids['list']:
        id_list.append(dic['ID'])


url = "http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsById"
for id in id_list:
    data = {
        'id': id
    }
    detail = requests.post(url=url, headers=headers, data=data).json()
    print(detail)
    all_data.append(detail)

json.dump(all_data, f, ensure_ascii=False)
f.close()