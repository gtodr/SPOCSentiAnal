# 登陆成功

import requests
data1={
    "fid":"434",
    "uname":"18956354215",
    "password":"faywencai881024",
    'refer': 'http%3A%2F%2Fysdxaqjy.aqjy.chaoxing.com',
    "t":"true"
}
session = requests.Session()
session.headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
    }
response1 = session.post("https://passport2.chaoxing.com/login", data=data1)
response1.encoding = response1.apparent_encoding
response = session.get('https://imooc.wljx.hfut.edu.cn/space/')

with open('xxt.html', 'wb') as f:
    f.write(response.content)