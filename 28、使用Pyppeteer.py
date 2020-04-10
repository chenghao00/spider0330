import asyncio
from pyppeteer import launch
from pyquery import PyQuery as pq


async def main():  # 默认使用async异步
    browser = await launch()  # 启动chromium，新建一个 Browser 对象
    page = await browser.newPage()  # 打开一个选项卡
    await page.goto('https://dynamic2.scrape.cuiqingcai.com/')
    await page.waitForSelector('.item .name')  # 等待加载
    doc = pq(await page.content())
    names = [item.text() for item in doc('.item .name').items()]
    print('Names:', names)
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())
