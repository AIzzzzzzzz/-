import requests
url="https://www.pearvideo.com/video_1745096"
contId=url.split("_")[1]
srcUrl= f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.9652466624651201"
resp=requests.get(srcUrl,headers={"user-agent":"Moziall/5.0","Referer": "https://www.pearvideo.com/video_1745096"})
dis=resp.json()
Urctime=dis["videoInfo"]["videos"]["srcUrl"]
sestemtime=dis['systemTime']
#"https://video.pearvideo.com/mp4/adshort/20211103/1636016870746-15791189_adpkg-ad_hd.mp4"
#https://video.pearvideo.com/mp4/adshort/20211103/cont-1745096-15791189_adpkg-ad_hd.mp4
srecUrl=Urctime.replace(sestemtime,f'cont-{contId}')
print(srecUrl)
with open("name.mp4","wb")as f:
    f.write(requests.get(srecUrl).content)
    print("over!!!")
