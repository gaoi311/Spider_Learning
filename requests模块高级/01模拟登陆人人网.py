import json

import requests

from lxml import etree

from requests模块高级.codeclass import YDMHttp


def getCodeText(imgPath, codetype):
    # 用户名
    username = '13956965930'

    # 密码
    password = 'a9026101'

    # 软件ＩＤ，开发者分成必要参数。登录开发者后台【我的软件】获得！
    appid = 10269

    # 软件密钥，开发者分成必要参数。登录开发者后台【我的软件】获得！
    appkey = '37f38526ce0b33bd4fb3f4d259079237'

    # 图片文件
    filename = imgPath

    # 验证码类型，# 例：1004表示4位字母数字，不同类型收费不同。请准确填写，否则影响识别率。在此查询所有类型 http://www.yundama.com/price.html
    codetype = codetype

    # 超时时间，秒
    timeout = 20
    result = None
    # 检查
    if (username == 'username'):
        print('请设置好相关参数再测试')
    else:
        # 初始化
        yundama = YDMHttp(username, password, appid, appkey)

        # 登陆云打码
        uid = yundama.login()
        print('uid: %s' % uid)

        # 查询余额
        balance = yundama.balance()
        print('balance: %s' % balance)

        # 开始识别，图片路径，验证码类型ID，超时时间（秒），识别结果
        cid, result = yundama.decode(filename, codetype, timeout)
        print('cid: %s, result: %s' % (cid, result))
    return result


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
}
#
# url = "http://www.renren.com/SysHome.do"
# page_text = requests.get(url, headers).text
# tree = etree.HTML(page_text)

url = "http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2020231121739"

data = {
    'email': '13956965930',
    'icode': '',
    'origURL': 'http://www.renren.com/home',
    'domain': 'renren.com',
    'key_id': '1',
    'captcha_type': 'web_login',
    'password': '71b799f5e44a6c9d120bab349bf63719f7d157566475eccd06d18865f11b6287',
    'rkey': '416f979466d9e3580aae016b1363f268',
    'f': 'http%3A%2F%2Fwww.renren.com%2F877762395'
}

session = requests.Session()

page_text = session.post(url=url, headers=headers, data=data).json()
url = page_text['homeUrl']

page_text = session.get(url=url, headers=headers).text
with open("renren.html", "w", encoding="utf-8") as f:
    f.write(page_text)
