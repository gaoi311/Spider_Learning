from selenium import webdriver
from selenium.webdriver import ActionChains
import time
bro = webdriver.Chrome(executable_path=r'E:\PythonFiles\Project\爬虫\selenium模块应用\chromedriver.exe')

bro.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')

bro.switch_to_frame('iframeResult')
div = bro.find_element_by_id('draggable')

action = ActionChains(bro)

action.click_and_hold(div)

for i in range(5):
    action.move_by_offset(17, 0).perform()
    time.sleep(0.3)

action.release()
print(div)