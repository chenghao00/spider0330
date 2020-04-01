import requests


class TiebaSpider:
    def __init__(self, tieba_name):
        self.tieba_name = tieba_name
        self.url_temp = 'https://tieba.baidu.com/f?kw=' + self.tieba_name + '&ie=utf-8&pn={}'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

    def get_url_list(self):  # 1、构造url列表
        # url_list = []
        # for i in range(5):
        #     url_list.append(self.url_temp.format(i * 50))
        # return url_list
        # 直接使用列表推倒式,在[]中也可以写if 得到条件的self.url_temp.format(i * 50)
        return [self.url_temp.format(i * 50) for i in range(5)]

    def parse_url(self, url):  # 发送请求、获取相应
        print(url)
        res = requests.get(url, headers=self.headers)
        return res.content

    def save_html(self, html_str, page_num):  # 保存html字符串
        file_path = 'save_html/{}-第{}页.html'.format(self.tieba_name, page_num)
        with open(file_path, 'wb') as f:
            f.write(html_str)

    def run(self):  # 实现主要逻辑
        # 1、构造url列表
        url_list = self.get_url_list()
        # 2、遍历，发送请求、获取相应
        for url in url_list:
            html_str = self.parse_url(url)
            # 3、保存
            page_num = url_list.index(url) + 1
            self.save_html(html_str, page_num)


if __name__ == '__main__':
    tieba_spider = TiebaSpider('python')
    tieba_spider.run()
