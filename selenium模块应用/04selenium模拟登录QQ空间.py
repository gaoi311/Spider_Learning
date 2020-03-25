from selenium import webdriver
import time
bro = webdriver.Chrome(executable_path=r'E:\PythonFiles\Project\爬虫\selenium模块应用\chromedriver.exe')

bro.get("https://qzone.qq.com/")

bro.switch_to_frame('login_frame')
a_tag = bro.find_element_by_id('switcher_plogin')
a_tag.click()

name = bro.find_element_by_id('u')
passsword = bro.find_element_by_id('p')

name.send_keys("2536745674")
passsword.send_keys("password")
btn = bro.find_element_by_id('login_button')

btn.click()

time.sleep(10)

