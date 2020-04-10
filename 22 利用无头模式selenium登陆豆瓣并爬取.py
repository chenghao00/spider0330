import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyquery import PyQuery as pq
from selenium.webdriver import ChromeOptions

#使用selenium，一定要使用time.sleep() 不然可能无法读出数据
class Douban:
    def __init__(self):
        self.url='https://book.douban.com/'
        #使用无头模式
        self.option = ChromeOptions()
        self.option.add_argument('--headless')
        self.browser=webdriver.Chrome('/Users/narihiro/opt/anaconda3/lib/python3.7/site-packages/selenium/webdriver/chrome/chromedriver',options=self.option)

    def login_in(self):
        self.browser.get(self.url)
        time.sleep(1)
        self.browser.find_element_by_class_name('nav-login').click()
        time.sleep(1)
        self.browser.find_element_by_class_name('account-tab-account').click()

        self.browser.find_element_by_id('username').send_keys('账号')

        self.browser.find_element_by_id('password').send_keys('密码')
        time.sleep(1)
        self.browser.find_element_by_class_name('account-form-field-submit').click()
        time.sleep(2)
        a_list=self.browser.find_elements_by_css_selector('.nav-items ul li')
        a_list[3].click()
        html_str=self.browser.page_source
        doc=pq(html_str)
        kinds=doc('.tagCol').text()
        print(kinds,type(kinds))
        time.sleep(1)

    def __del__(self):
        '''调用内建的稀构方法，在程序退出的时候自动调用
        类似的还可以在文件打开的时候调用close，数据库链接的断开
        '''
        self.browser.close()


if __name__ == '__main__':
    douban=Douban()
    douban.login_in()



