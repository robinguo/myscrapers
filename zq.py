import requests
import json

urltemplate = 'http://fund.eastmoney.com/data/FundGuideapi.aspx?dt=0&ft=zq&sd=&ed=&tp=46837d8661373bec&sc=3y&st=desc&pi=pageindex&pn=20&zf=diy&sh=list'
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

f = open('zq.txt', 'a')
for data in datas:
    f.write(data + '\n')
f.close()