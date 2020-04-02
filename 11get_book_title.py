import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
res = requests.get('https://book.douban.com/', headers=headers)
#print(res.content.decode())
pattern=re.compile('<a.*?href="(.*?)".*?title="(.*?)">.*?</a>',re.S)
results=re.findall(pattern,res.text)
print(results)

