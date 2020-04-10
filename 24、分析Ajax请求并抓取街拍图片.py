import requests
from urllib.parse import urlencode
from selenium import webdriver
import time
from pyquery import PyQuery as pq
from selenium.webdriver import ChromeOptions


def get_page_index(offset, keyword):
    data = {
        'aid': 24,
        'app_name': 'web_search',
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': 20,
        'en_qc': 1,
        'cur_tab': 1,
        'from': 'search_tab',
        'pd': 'synthesis',
        # 'timestamp': '1586247629154',
        # '_signature':'v7v7OAAgEBCGRSmDayYhEr - 6uiAAOFFPhFTTiIwaq6WpnrFECcQ4BliwES9x1dXo9zelv9FPNlBa3h8MGjFBe4z173zCgJ5FHgid5M20OKjpkGyKJ - 8pZpMpjzdE - h02UlO'
    }
    url = 'https://www.toutiao.com/search/?' + urlencode(data)
    print(url)
    browser = webdriver.Chrome(
        '/Users/narihiro/opt/anaconda3/lib/python3.7/site-packages/selenium/webdriver/chrome/chromedriver')
    # browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
    #     'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'
    # })
    browser.get(url)
    time.sleep(5)
    html_str = browser.page_source

    # res = requests.get(url)
    # if res.status_code == 200:
    #     return res.text
    doc = pq(html_str)
    # print(doc)
    hrefs = doc('.link').items()
    for href in hrefs:
        params = href.parent().find('a').attr('href')[7:]
        a_url = 'https://www.toutiao.com/a' + params
        yield a_url


def parse_page_detail(href):
    # option = ChromeOptions()
    # option.add_argument('--headless')
    browser = webdriver.Chrome(
        '/Users/narihiro/opt/anaconda3/lib/python3.7/site-packages/selenium/webdriver/chrome/chromedriver')  # ,options=option
    browser.get(href)
    # print(browser.page_source)
    doc = pq(browser.page_source)
    title = doc('.bui-right').find('h2').text()
    return title


def main():
    hrefs = get_page_index(80, '街拍')
    for href in hrefs:
        title = parse_page_detail(href)
        print(title)


if __name__ == '__main__':
    main()
