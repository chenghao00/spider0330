import requests

res = requests.get('http://www.baidu.com')
# 指定编码方式encoding='utf-8'，正确显示res.text ！！推测解码
res.encoding = 'utf-8'
print(res.text)
print('-' * 100)
# 第二种获取方式，res.content，它是bytes 需解码decode() 一般用res.content
print(res.content.decode())


img=requests.get('https://upload-images.jianshu.io/upload_images/14132861-2c310f570bb32fb2.png?imageMogr2/auto-orient/strip|imageView2/2/w/912')
with open('picture.png','wb') as f:
    f.write(img.content)