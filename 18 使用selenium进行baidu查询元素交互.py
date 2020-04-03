from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

try:
    browser=webdriver.Chrome(executable_path='/Users/narihiro/opt/anaconda3/lib/python3.7/site-packages/selenium/webdriver/chrome/chromedriver')
    browser.get('http://www.baidu.com')
    input_first=browser.find_element_by_id('kw')
    input_first.send_keys('想你呦')
    time.sleep(2)
    input_first.clear()
    input_first.send_keys('babe！')
    button=browser.find_element_by_id("su")
    button.click()
    #获取文本值
    input=browser.find_element_by_class_name('toindex')
    print(input.text)
    print(input.id)
    print(input.location)
    print(input.tag_name)
    print(input.size)
    time.sleep(5)
finally:
    browser.close()
