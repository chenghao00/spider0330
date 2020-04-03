from selenium import webdriver
from selenium.webdriver import ActionChains

#更多操作: http://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.common.action_chains
browser = webdriver.Chrome('/Users/narihiro/opt/anaconda3/lib/python3.7/site-packages/selenium/webdriver/chrome/chromedriver')
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')
source = browser.find_element_by_css_selector('#draggable')
target = browser.find_element_by_css_selector('#droppable')
actions = ActionChains(browser)
actions.drag_and_drop(source, target)
actions.perform()