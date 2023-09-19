import requests
n=0
url='https://www.bh3.com/content/bh3Cn/getContentList?pageSize=9&pageNum=1&channelId=177'
for i in range(7):
    param={
        'pageSize':'9',
        'pageNum':i+1,
        'channelId':'177',
    }



    r=requests.get(url,params=param)
    for i in range(9):
        page=r.json()['data']['list'][i]['ext'][0]['value'][0]['url']
        png_name=page.split('/')[-1]
        with open(png_name,'wb') as f:
            f.write(requests.get(page).content)
            n=n+1

            print(f'正在窃取第{n}张图片')
            print('已完成窃取')







