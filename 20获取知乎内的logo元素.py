from selenium import webdriver
from selenium.webdriver import ActionChains
#获取属性
browser = webdriver.Chrome('/Users/narihiro/opt/anaconda3/lib/python3.7/site-packages/selenium/webdriver/chrome/chromedriver')
url = 'https://www.zhihu.com/explore'
browser.get(url)
logo = browser.find_element_by_tag_name('svg')
print(logo)
print(logo.get_attribute('fill'))

