# 爬虫-带密码登陆

import requests
data1={
    "fid":"1366",
    "uname":"18956354215",
    "password":"faywencai881024",
    "t":"true"
}
session = requests.Session()
session.headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
    }
response1 = session.post("http://passport2.chaoxing.com/fanyalogin", data=data1)
response1.encoding = response1.apparent_encoding
response = session.get('https://imooc.wljx.hfut.edu.cn/space/index?t=1711805418513')