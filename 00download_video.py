from pyquery import PyQuery as pq
import re
import json
import requests


class Downloadvideo:
    def __init__(self, key_name,file):
        self.key_name = key_name
        self.file = file
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
        # 搜索内容返回的url
        self.url_temp = 'https://v.qq.com/x/search/?q=' + self.key_name + '&needCorrect=' + self.key_name + '&stag=3&' \
            # 下载视频视频解析接口的url请求地址
        self.url = 'http://vv.video.qq.com/getinfo?vids={}&platform=101001&charge=0&otype=json'

    def get_url_list(self):
        return [self.url_temp.format(i) for i in range(1, 2)]

    def parse_url(self, url):
        doc = pq(url)
        # 获取a标签的父级所在的div,多个元素用items()
        div_tags = doc('.result_title').items()
        vids=[]
        for div_tag in div_tags:
            # 获取div的子元素a中的href属性值
            href = div_tag.find('a').attr('href')
            # print(href)
            # 正则提取出vid用于视频下载
            if 'qq' in href and 'page' in href:
                pattern = re.compile('page/(.*?).html', re.S)
                vid = re.findall(pattern, href)[0]
                # return re.findall(pattern, href)[0]
                vids.append(vid)
        return vids


    def parse_vid(self, vid):
        # 直接使用视频解析接口，只需传入vid
        url = self.url.format(vid)
        doc2 = pq(url)
        # print(type(doc2.html()))
        # print(doc2.html())
        # 处理数据
        result = doc2.html().replace('QZOutputJson=', '').replace(';', '')
        # print(result,type(result))
        result = json.loads(result)
        # print(result)
        try:
            titles=[]
            for i in result['vl']['vi']:
                vkey = i['fvkey']
                title = i['ti']
                fn = i['fn']
                url3 = i['ul']['ui'][2]['url']
                #print(vkey, title, fn, url3)
                #print(title)
                self.DownLoad(vkey,title,fn,url3)
                titles.append(title)
        except:
            pass

        finally:
            return titles

    def DownLoad(self, vkey, title, fn, url):
        # 拼接成下载地址
        url = url + fn + '?vkey=' + vkey
        #下载大文件使文件完整下载stream=True
        res = requests.get(url, stream=True, headers=self.headers)
        with open('{0}/{1}.mp4'.format(self.file, title), 'ab')as f:
            f.write(res.content)
            f.flush()

    def run(self):
        results=[]
        # 1、构造url列表，收集要下载的地址，每页的url由6个参数组成，其中ses可以去掉，q和needCorrect都是要搜索的关键词“病毒 教育”，stage是固定值，cur是当前页码，cxt是固定值，
        url_list = self.get_url_list()
        # 2、遍历，发送请求、获取相应
        for url in url_list:
            # 解析url得到vids
            vids = self.parse_url(url)
            # 解析vid得到视频,并保存
            for vid in vids:
                result=self.parse_vid(vid)
                results.append(result)
        return results

if __name__ == '__main__':
    download=Downloadvideo('病毒教育','save_video')
    download.run()


