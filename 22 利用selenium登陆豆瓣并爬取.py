import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Douban:
    def __init__(self):
        self.url='https://book.douban.com/'
        self.browser=webdriver.Chrome('/Users/narihiro/opt/anaconda3/lib/python3.7/site-packages/selenium/webdriver/chrome/chromedriver')

    def login_in(self):
        self.browser.get(self.url)
        time.sleep(2)
        self.browser.find_element_by_class_name('nav-login').click()
        time.sleep(2)
        self.browser.find_element_by_class_name('account-tab-account').click()
        time.sleep(2)
        self.browser.find_element_by_id('username').send_keys('18515097731')
        time.sleep(2)
        self.browser.find_element_by_id('password').send_keys('111')
        time.sleep(2)
        self.browser.find_element_by_class_name('account-form-field-submit').click()
        time.sleep(2)
        print(self.driver.get_cookies())
        time.sleep(2)

    def __del__(self):
        '''调用内建的稀构方法，在程序退出的时候自动调用
        类似的还可以在文件打开的时候调用close，数据库链接的断开
        '''
        self.browser.close()


if __name__ == '__main__':
    douban=Douban()
    douban.login_in()



