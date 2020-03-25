import requests
from hashlib import md5
from selenium import webdriver
from lxml import etree
import time
from PIL import Image
from selenium.webdriver import ActionChains


class Chaojiying_Client:
    def __init__(self, username, password, soft_id):
        self.username = username
        password = password.encode('utf8')
        self.password = md5(password).hexdigest()
        self.soft_id = soft_id
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }

    def PostPic(self, im, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
        }
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files, headers=self.headers)
        return r.json()

    def ReportError(self, im_id):
        """im_id:报错题目的图片ID."""
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
        return r.json()

bro = webdriver.Chrome(executable_path=r'E:\PythonFiles\Project\爬虫\selenium模块应用\chromedriver.exe')
bro.maximize_window()
bro.get('https://kyfw.12306.cn/otn/resources/login.html')

page_text = bro.page_source
login = bro.find_element_by_xpath('/html/body/div[2]/div[2]/ul/li[2]/a')
login.click()

bro.save_screenshot("aa.png")

code_img = bro.find_elements_by_xpath('//*[@id="J-loginImg"]')[0]

location = code_img.location
size = code_img.size

rangle = (
    int(location['x']),
    int(location['y']),
    int(location['x'] + size['width']),
    int(location['y'] + size['height'])
)

i = Image.open('aa.png')
code_img_name = 'code.png'
frame = i.crop(rangle)
frame.save(code_img_name)

chaojiying = Chaojiying_Client('13956965930', 'password', '	904062')
im = open('code.png', 'rb').read()
result = chaojiying.PostPic(im, 9004)['pic_str']

all_list = []

if '|' in result:
    list_1 = result.split('|')
    count_1 = len(list_1)
    for i in range(count_1):
         xy_list = []
         x = int(list_1[i].split(',')[0])
         y = int(list_1[i].split(',')[1])
         xy_list.append(x)
         xy_list.append(y)
         all_list.append(xy_list)
else:
    x = int(result.split(',')[0])
    y = int(result.split(',')[1])
    xy_list = []
    xy_list.append(x)
    xy_list.append(y)
    all_list.append(xy_list)
print(all_list)

for l in all_list:
    x = l[0]
    y = l[1]
    ActionChains(bro).move_to_element_with_offset(code_img, x, y).click().perform()
    time.sleep(1)
    bro.find_element_by_id('J-userName').send_keys('13956965930')
    bro.find_element_by_id('J-password').send_keys('password')
    time.sleep(1)
    bro.find_element_by_id('J-login').click()
