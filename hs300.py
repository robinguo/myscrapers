import requests
import json

urltemplate = 'http://fund.eastmoney.com/data/FundGuideapi.aspx?dt=0&ft=zs&sd=&ed=&tp=104adc77fa93e271&sc=3y&st=desc&pi=pageindex&pn=20&zf=diy&sh=list'
url = urltemplate.replace('pageindex', "1")
response = requests.get(url)
res = response.text.split('=')[1]

datas = json.loads(res)['datas']
pagenum = json.loads(res)['allPages']

for p in range(2, int(pagenum) + 1):
    url = urltemplate.replace('pageindex', str(p))
    response = requests.get(url)
    res = response.text.split('=')[1]
    datas = datas + json.loads(res)['datas']

f = open('hs300.txt', 'a')
for data in datas:
    f.write(data + '\n')
f.close()