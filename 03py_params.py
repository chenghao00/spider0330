import requests
url='https://www.baidu.com/s?'
headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
params={'wd':'python'}

res=requests.get(url,headers=headers,params=params)
print(res.status_code)
print(res.request.url)
