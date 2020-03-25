import requests
from lxml import etree

from 验证码.codeclass import YDMHttp


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
        uid = yundama.login();
        print('uid: %s' % uid)

        # 查询余额
        balance = yundama.balance();
        print('balance: %s' % balance)

        # 开始识别，图片路径，验证码类型ID，超时时间（秒），识别结果
        cid, result = yundama.decode(filename, codetype, timeout);
        print('cid: %s, result: %s' % (cid, result))
    return result
    ######################################################################

if __name__ == '__main__':
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
    }
    url = "https://so.gushiwen.org/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx"
    page_text = requests.get(url=url, headers=headers).text

    tree = etree.HTML(page_text)
    code_img_src = "https://so.gushiwen.org" + tree.xpath("//*[@id='imgCode']/@src")[0]
    img_data = requests.get(url=code_img_src, headers=headers).content
    print(img_data)

    with open("code.jpg", "wb") as f:
        f.write(img_data)

    print(getCodeText('code.jpg', 1004))