from selenium import webdriver
from time import sleep
bro = webdriver.Chrome(executable_path=r'E:\PythonFiles\Project\爬虫\selenium模块应用\chromedriver.exe')

bro.get("https://www.taobao.com/")
print(000)

search_input = bro.find_element_by_class_name('search-combobox-input')
print(111)
search_input.send_keys("Iphone")

bro.execute_script("window.scrollTo(0,document.body.scrollHeight)")
sleep(2)
btn = bro.find_element_by_class_name('btn-search')
print(222)
btn.click()

# sleep(10)
# bro.quit()