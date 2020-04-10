import asyncio
from pyppeteer import launch
from pyquery import PyQuery as pq
from config import *
import requests
import json
import re
width, height = 1366, 768


# 返回一个协程
async def main(total_page):
    # 启动浏览器
    browser = await launch(headless=False,
                           args=['--disable-infobars', f'--window-size={width},{height}'])
    # 新建一个选项卡
    page = await browser.newPage()

    # todo:同时设置了浏览器窗口的宽高以及显示区域的宽高
    await page.setViewport({'width': width, 'height': height})

    # todo:是页面不被检测webdriver
    await page.evaluateOnNewDocument('Object.defineProperty(navigator,"webdriver",{get:()=>undefined})')

    await page.goto('https://www.tmall.com/')

    # 等待加载
    await page.waitForSelector('#mq')
    # 输入keyword
    await page.type('#mq', KEYWORD)

    # 等待加载
    await page.waitForSelector('#mallSearch > form > fieldset > div > button')
    # 点击
    await page.click('#mallSearch > form > fieldset > div > button')

    # 获取页面源码
    print('这是第1页')
    await page.waitForSelector('#J_ItemList')
    html_str = await page.content()
    get_products(html_str)

    # 实现翻页
    for i in range(2, total_page + 1):
        print('这是第{}页'.format(i))
        # 等待加载
        await page.waitForSelector('.ui-page-next')
        # 输入keyword
        await page.click('.ui-page-next')

        # 获取页面源码
        await page.waitForSelector('#J_ItemList')
        html_str = await page.content()
        get_products(html_str)

    await asyncio.sleep(100)
    await browser.close()


def get_products(html_str):
    doc = pq(html_str)
    items = doc('#J_ItemList .product').items()
    for item in items:
        # print(item.html())
        content = {
            '名字': item.find('.productTitle a').attr('title'),
            '价格': item.find('.productPrice em').text(),
            '店名': item.find('.productShop-name').text(),
            '月成交量': item.find('.productStatus em').text(),
            '评价数': item.find('.productStatus em').text(),
            '天猫链接': 'https:' + item.find('.productTitle a').attr('href'),
        }

        src=item.find('.productImg-wrap a').html()  # [24:-4]
        pattern = re.compile('img.alicdn.com(/.*)+.jpg', re.S)
        results = re.findall(pattern,src)
        for result in results:
            pic_url = 'https://img.alicdn.com'+result+'.jpg'
            pic_name = item.find('.productTitle a').attr('title')
            print(content, pic_url)
            save_pic(pic_url,pic_name)
            save_text(content)

def save_text(content):
    with open('msg_dogcloth.txt', 'a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')


def save_pic(pic_url,pic_name):
    res = requests.get(pic_url)
    with open('dogcloth_pic/{}.png'.format(pic_name), 'wb') as f:
        f.write(res.content)


asyncio.get_event_loop().run_until_complete(main(2))
