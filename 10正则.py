import re
# \w	匹配字母数字及下划线
# \W	匹配非字母数字下划线
# \s	匹配任意空白字符，等价于 [\t\n\r\f].
# \S	匹配任意非空字符
# \d	匹配任意数字，等价于 [0-9]
# \D	匹配任意非数字
# \A	匹配字符串开始
# \Z	匹配字符串结束，如果是存在换行，只匹配到换行前的结束字符串
# \z	匹配字符串结束
# \G	匹配最后匹配完成的位置
# \n	匹配一个换行符
# \t	匹配一个制表符
# ^	匹配字符串的开头
# $	匹配字符串的末尾。
# .	匹配任意字符，除了换行符，当re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符。
# [...]	用来表示一组字符,单独列出：[amk] 匹配 'a'，'m'或'k'
# [^...]	不在[]中的字符：[^abc] 匹配除了a,b,c之外的字符。
# *	匹配0个或多个的表达式。
# +	匹配1个或多个的表达式。
# ?	匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式
# {n}	精确匹配n个前面表达式。
# {n, m}	匹配 n 到 m 次由前面的正则表达式定义的片段，贪婪方式
# a|b	匹配a或b
# ( )	匹配括号内的表达式，也表示一个组

#贪婪匹配
import re

content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^He.*(\d+).*Demo$', content)
print(result)
print(result.group(1))

#非贪婪匹配
content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^He.*?(\d+).*Demo$', content)
print(result)
print(result.group(1))

#todo:若有换行符 使用re.S可以使.匹配,匹配模式，
content = '''Hello 1234567 World_This
is a Regex Demo
'''
result = re.match('^He.*?(\d+).*?Demo$', content, re.S)
print(result.group(1))


#转义
import re

content = 'price is $5.00'
result = re.match(r'price is \$5\.00', content)
print(result)


#todo:关于re.search(),扫描整个字符串并返回第一个成功的匹配。
import re

html = '''<div id="songs-list">
    <h2 class="title">经典老歌</h2>
    <p class="introduction">
        经典老歌列表
    </p>
    <ul id="list" class="list-group">
        <li data-view="2">一路上有你</li>
        <li data-view="7">
            <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
        </li>
        <li data-view="4" class="active">
            <a href="/3.mp3" singer="齐秦">往事随风</a>
        </li>
        <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
        <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
        <li data-view="5">
            <a href="/6.mp3" singer="邓丽君"><i class="fa fa-user"></i>但愿人长久</a>
        </li>
    </ul>
</div>'''
result = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>', html, re.S)
if result:
    print(result.group(1), result.group(2))


#todo:re.findall()搜索字符串，以列表形式返回全部能匹配的子串。
import re

html = '''<div id="songs-list">
    <h2 class="title">经典老歌</h2>
    <p class="introduction">
        经典老歌列表
    </p>
    <ul id="list" class="list-group">
        <li data-view="2">一路上有你</li>
        <li data-view="7">
            <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
        </li>
        <li data-view="4" class="active">
            <a href="/3.mp3" singer="齐秦">往事随风</a>
        </li>
        <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
        <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
        <li data-view="5">
            <a href="/6.mp3" singer="邓丽君">但愿人长久</a>
        </li>
    </ul>
</div>'''
results = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>', html, re.S)
print(results)
print(type(results))
for result in results:
    print(result)
    print(result[0], result[1], result[2])


#re.compile()将正则字符串编译成正则表达式对象
content='''<a class="" href="https://book.douban.com/subject/34970027/?icn=index-latestbook-subject"
                  title="第十二张牌">第十二张牌</a>'''
pattern=re.compile('<a.*?href="(.*?)".*?title="(.*?)">.*?</a>',re.S)
results=re.findall(pattern,content)
for result in results:
    file_path = 'save_html/{}.txt'.format('豆瓣图书链接与作者')
    with open(file_path, 'w') as f:
        f.write(result[0]+':')
        f.write(result[1])