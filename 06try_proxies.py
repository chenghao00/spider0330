# coding=utf-8
import requests

#准备ip池，随机选择使用
#高匿可用代理proxies = {"http":"http://103.38.41.90:1081"}
proxies = {'http': 'http://123.56.17.105:7731'}
headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

r = requests.get("http://www.baidu.com",proxies=proxies,headers=headers)
print(r.status_code)
print(r.content.decode())