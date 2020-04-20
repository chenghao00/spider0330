from pyquery import PyQuery as pq
import json
import requests

# doc = pq('https://view.inews.qq.com/g2/getOnsInfo?name=disease_other')
doc = requests.get('https://view.inews.qq.com/g2/getOnsInfo?name=disease_other')
# print(doc.text())
json_data = json.loads(doc.text)
json_data = json.loads(json_data['data'])
chinaDayList = json_data['chinaDayList']
# print(chinaDayList)

date_list = []
confirm_data = []
json_datas = {}

for data in chinaDayList:
    # 处理成列表格式
    date_list.append(data['date'])
    confirm_data.append(data['confirm'])

    # 处理成json格式
    date = data['date']
    confirm = data['confirm']
    json_datas[date] = confirm

print(date_list, confirm_data, json_datas)
