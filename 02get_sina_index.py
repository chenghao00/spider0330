import requests
#设置请求头
headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
#res=requests.get('https://www.sina.com.cn/',headers=headers)
res=requests.get('https://www.baidu.com/',headers=headers)

#print(res.text)

print(res.content.decode())

# print(res.headers)
# print(res.request.url)
# print(res.request.headers)