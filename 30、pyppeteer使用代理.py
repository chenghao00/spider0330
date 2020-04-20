# import asyncio
# from pyppeteer import launch
#
# proxy = '123.56.17.105:7731'
#
#
# async def main():
#     browser = await launch({'args': ['--proxy-server=http://' + proxy], 'headless': False})
#     page = await browser.newPage()
#     await page.goto('https://httpbin.org/get')
#     print(await page.content())
#     await browser.close()
#
#
# if __name__ == '__main__':
#     asyncio.get_event_loop().run_until_complete(main())


from config import *
from selenium import webdriver

proxy = '123.56.17.105:7731'
options = webdriver.ChromeOptions()
options.add_argument('--proxy-server=http://' + proxy)
browser = webdriver.Chrome(executable_path=Executable_path,options=options)
browser.get('https://httpbin.org/get')
print(browser.page_source)
browser.close()