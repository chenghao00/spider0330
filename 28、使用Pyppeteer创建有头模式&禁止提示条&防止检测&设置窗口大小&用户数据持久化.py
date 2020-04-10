import asyncio
from pyppeteer import launch
from pyquery import PyQuery as pq

width, height = 1366, 768


async def main():  # 默认使用async异步
    # '--disable-infobars'禁止提示条
    # userDataDir='./userdata'用户数据持久化
    browser = await launch(headless=False,
                           userDataDir='./userdata',
                           args=['--disable-infobars', f'--window-size={width},{height}'])  # 启动chromium，新建一个 Browser 对象

    ## todo：创建无痕模式不与其他的浏览器示例共享 Cache、Cookies 等内容
    ## context = await browser.createIncognitoBrowserContext()
    ## page = await context.newPage()

    page = await browser.newPage()  # 打开一个选项卡

    # todo:同时设置了浏览器窗口的宽高以及显示区域的宽高
    await page.setViewport({'width': width, 'height': height})

    # todo:是页面不被检测webdriver
    await page.evaluateOnNewDocument('Object.defineProperty(navigator,"webdriver",{get:()=>undefined})')

    await page.goto('https://antispider1.scrape.cuiqingcai.com/')

    await page.waitForSelector('.item .name')  # 等待加载
    doc = pq(await page.content())
    names = [item.text() for item in doc('.item .name').items()]
    print('Names:', names)
    await asyncio.sleep(100)
    await browser.close()


# main()--> 不会直接运行，而是返回了一个 coroutine 协程对象
# 使用 get_event_loop 方法创建了一个事件循环 loop，
# 并调用了 loop 对象的 run_until_complete 方法将协程注册到事件循环 loop 中，然后启动。
asyncio.get_event_loop().run_until_complete(main())
