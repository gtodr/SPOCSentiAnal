# 登陆成功但仍显示登陆页面-爬虫

import requests

# 设置登录的URL
login_url = 'http://passport2.chaoxing.com/fanyalogin'
# 设置POST的数据，这通常是用户名和密码
login_data = {
    "fid":"1366",
    "uname":"18956354215",
    "password":"faywencai881024",
    "t":"true"}

# 发送POST请求
session = requests.Session()
session.headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
    }
response = session.post(login_url, data=login_data)

# 检查响应状态
if response.status_code == 200:
    print("登录成功")
else:
    print("登录失败")

# 获取你想要爬取的页面内容
content_url = 'https://imooc.wljx.hfut.edu.cn/space/index?t=1711805418513'
content = session.get(content_url).content.decode('utf-8')
print(content)