import requests
from bs4 import BeautifulSoup
url="https://www.umei.cc/"
r=requests.get(url,verify=False,headers={"user-agent":"Moziall/5.0"})
r.encoding=r.apparent_encoding
Soup=BeautifulSoup(r.text,"html.parser")
href_1=Soup.find("div",class_="SpecBox indexSpec fc").find_all("a")
for it in href_1:
    png_href=it.get('href').strip("/")
    page=url+png_href    
    png=requests.get(page)
    png.encoding="utf-8"
    child_png=BeautifulSoup(png.text,"html.parser")
    child_png_drow=child_png.find("div",class_="TypeList").find_all("img")
    for itt in child_png_drow:
        
        drowpng=itt.get('src')
        img=requests.get(drowpng)
        img_name=drowpng.split("/")[-1]
        with open(img_name,"wb")as f:
            f.write(img.content)
            print("over!!")
        
    #print(png.text[:1000])
   
    #print(png_href)
