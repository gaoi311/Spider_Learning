from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

from selenium.webdriver import ChromeOptions
option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
bro = webdriver.Chrome(executable_path=r'E:\PythonFiles\Project\爬虫\selenium模块应用\chromedriver.exe', chrome_options=chrome_options, options=option)
bro.get('http://www.baidu.com')
print(bro.page_source)
