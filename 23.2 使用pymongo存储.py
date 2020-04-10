from pyquery import PyQuery as pq
from selenium import webdriver
import time
import requests
import json
from multiprocessing import Pool
import pymongo
#
# #通过selenium获取网页信息
# # browser = webdriver.Chrome(executable_path='/Users/narihiro/opt/anaconda3/lib/python3.7/site-packages/selenium/webdriver/chrome/chromedriver')
# # browser.get('http://maoyan.com/board')
# # html_str=browser.page_source
# #print(type(html_str))
# #解析获取名称、主演、上映时间、评分、图片链接
# doc=pq(filename='save_html/maoyan.html')
# all_dd=doc('.board-wrapper').children() #.items()
# print(all_dd)
# # for dd in all_dd:
# #     title=dd.find('a').attr('title')
# #     #pic=
# # browser.close()



def get_one_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    res = requests.get(url,headers=headers)
    if res.status_code == 200:
        #print(res.text)
        return res.text

#解析获取名称、主演、上映时间、评分、图片链接
def parse_one_page(html):
    doc = pq(html)
    all_dd = doc('.board-wrapper').children().items()
    #print(all_dd)
    for dd in all_dd:
        yield {
            'id':dd.find('.board-index').text(),
            'title':dd.find('a').attr('title'),
            'star_name':dd.find('.star').text()[3:],
            'pic':dd.find('.board-img').attr('src'),
            'time':dd.find('.releasetime').text()[5:],
            'score':dd.find('.integer').text()+dd.find('.fraction').text()

        }

def save_one_to_file(item):
    MONGO_CONNECTION_STRING='mongodb://localhost:27017/'
    MONGO_DB_NAME='movies'
    MOGO_COLLECTION_NAME='movies'
    client=pymongo.MongoClient(MONGO_CONNECTION_STRING)
    db=client.movies
    colletion=db.movies
    result=colletion.insert_one(item)
    print(result.inserted_id)

def main(offset):
    url='https://maoyan.com/board/4?offset='+str(offset)
    html=get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        save_one_to_file(item)

if __name__ == '__main__':
    for i in range(10):
        main(i*10)
    # pool=Pool()
    # pool.map(main,[i*10 for i in range(10)])


