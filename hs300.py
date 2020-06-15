import requests
import json

urltemplate = 'https://fundapi.eastmoney.com/fundtradenew.aspx?ft=zs&sc=1n&st=desc&pi=pageindex&pn=100&cp=&ct=&cd=&ms=&fr=053&plevel=&fst=&ftype=&fr1=052&fl=0&isab=1'
url = urltemplate.replace('pageindex', "1")
response = requests.get(url)
res = response.text.split('=')[1][:-1]
res = res.replace('datas', '"datas"')
res = res.replace('allRecords', '"allRecords"')
res = res.replace('pageIndex', '"pageIndex"')
res = res.replace('pageNum', '"pageNum"')
res = res.replace('allPages', '"allPages"')

datas = json.loads(res)['datas']
pagenum = json.loads(res)['allPages']

for p in range(2, pagenum + 1):
    url = urltemplate.replace('pageindex', str(p))
    response = requests.get(url)
    res = response.text.split('=')[1][:-1]
    res = res.replace('datas', '"datas"')
    res = res.replace('allRecords', '"allRecords"')
    res = res.replace('pageIndex', '"pageIndex"')
    res = res.replace('pageNum', '"pageNum"')
    res = res.replace('allPages', '"allPages"')
    datas = datas + json.loads(res)['datas']

f = open('hs300.txt', 'a')
for data in datas:
    f.write(data + '\n')
f.close()