import requests
''' function a(a=16) {  #随机的16个字符串
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)#循环16次
            e = Math.random() * b.length,#随机数1.2
            e = Math.floor(e),取整1
            c += b.charAt(e);取字符串中1的位置
        return c
    }
    function b(a, b) {
        var c = CryptoJS.enc.Utf8.parse(b)
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)
          , f = CryptoJS.AES.encrypt(e, c, {
            iv: d,
            mode: CryptoJS.mode.CBC
        });
        return f.toString()
    }
    function c(a, b, c) {
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) {   d=数据，e=010001，f=很长的数据,g="0CoJUm6Qyw8W8jud"
        var h = {}  空对象
           i = a(16);  #i就是一个16位的随机值
        return h.encText = b(d, g),
        h.encText = b(h.encText, i), 
        h.encSecKey = c(i, e, f),
        h
    }'''

g="0CoJUm6Qyw8W8jud"
e="010001"
f="00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
i="MRfv4dmX9VoOTtS2"

def get_en():
    return "85fa4a4f99c68cd2b246834fa9f6f3b4ad136ce9fb5d2fd6f30372a028cbc68e3ef7448696c011840ddeff4644948f60ad06b1405d9436a45d74c7b61a90b9b49a0443071d720c918ca197d03711cffd09073ce7b54c5f528dac3e6db6bc3bbc753598173b6f0971a7a7f815da919b5e55266f23f8d6709ff1eb7d0c950c6185"


url="https://music.163.com/weapi/comment/resource/comments/get?csrf_token="
r=requests.post(url,headers={"user-agent":"Moziall/5.0"})
data={
    "csrf_token": "7c6e5c40d2a1feb12d6bb7e8bae0d06d"
    "cursor": "-1"
    "offset": "0"
    "orderType": "1"
    "pageNo": "1"
    "pageSize": "20"
    "rid": "A_PL_0_2829816518"
    "threadId": "A_PL_0_2829816518"
    }

