import gevent
from gevent import monkey
import requests
from pyquery import PyQuery as pq
import threading
from requests.packages.urllib3.util.ssl_ import create_urllib3_context

create_urllib3_context()
monkey.patch_all()  # 对所有io操作打上补丁，固定加这一句


def get_title(i):
    print(threading.current_thread().name)  # 打印出当前线程名称
    url = 'https://movie.douban.com/top250?start={}&filter='.format(i * 25)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    res = requests.get(url=url, headers=headers)
    doc = pq(res.text)
    ids = doc('.pic').items()
    for id in ids:
        print({id.text(): id.find('img').attr('alt')})


gevent.joinall([gevent.spawn(get_title, i) for i in range(10)])
