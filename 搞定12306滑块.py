from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
#嵌入js代码
option=Options()
option.add_experimental_option('excludeSwitches',['enable-automation'])
option.add_argument('--disable-blink-features=AutomationControlled')
web=Chrome(options=option)
#没有上一步无法实现拖拽浏览器，window.navigator.webdriver,浏览器必须是False
# 而通过selenium打开的是True

web.get('https://www.12306.cn/index/')
web.find_element(By.XPATH,'//*[@id="J-btn-login"]').click()
time.sleep(2)
web.find_element(By.XPATH,'//*[@id="J-userName"]').send_keys('13353610096')
web.find_element(By.XPATH,'//*[@id="J-password"]').send_keys('a84526381')
web.find_element(By.XPATH,'//*[@id="J-login"]').click()
time.sleep(3)
obj=web.find_element(By.XPATH,'//*[@id="nc_1_n1z"]')
ActionChains(web).drag_and_drop_by_offset(obj,300,0).perform()
