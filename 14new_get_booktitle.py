import requests
import re
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
res = requests.get('https://book.douban.com/', headers=headers)
file_path='save_html/{}.html'.format('bs4douban')
with open(file_path,'w') as f:
    f.write(res.text)

soup=BeautifulSoup(open(file_path),'lxml')
# for a in soup.select('.cover a[title]'):
#     print(a['title'])
title_list=[(a['href'],a['title']) for a in soup.select('.cover a[href][title]')]
with open('book_title.txt','w') as f:
    f.write(str(title_list))
