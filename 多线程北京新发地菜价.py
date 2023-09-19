import requests
from concurrent.futures import ThreadPoolExecutor
import csv
f=open("data2.csv","w",encoding="utf-8")
csvwriter=csv.writer(f)

def xiancheng(url):
    data = {

        "limit": "20",
        "current": i + 1,
        "pubDateStartTime": "",
        "pubDateEndTime": "",
        "prodPcatid": "",
        "prodCatid": "",
        "prodName": "",

    }
    a=[]
    r=requests.post(url,data=data)
    name=r.json()['list']
    for it in name:
        a.append(it['prodName'])
        a.append(it['lowPrice'])
        a.append(it['highPrice'])
        a.append(it['avgPrice'])
        print("\n\n")
    csvwriter.writerow(a)

if __name__== '__main__':
    with ThreadPoolExecutor(500) as t:
        for i in range(20143):
            t.submit(xiancheng,('http://www.xinfadi.com.cn/getPriceData.html'))
        
        
        
