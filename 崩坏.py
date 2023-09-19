import requests
from bs4 import BeautifulSoup
for it in range(7):
    
    url=f"https://www.bh3.com/content/bh3Cn/getContentList?pageSize=9&pageNum={it+1}&channelId=177"
    r=requests.get(url)
    for i in range(8):
        
        page_1=r.json()['data']['list'][i]['ext'][0]['value'][0]['url']
        png_name=page_1.split("/")[-1]

        with open(png_name,"wb") as f:
            f.write(requests.get(page_1).content)
            print("第{}抓取完成".format((i+1)*(it+1)))
        
