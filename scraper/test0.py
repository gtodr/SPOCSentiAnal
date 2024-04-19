# 豆瓣爬虫实验

import urllib.request, urllib.error
from bs4 import BeautifulSoup    
import re       
import csv

#爬取网页
def analyze_html(baseurl):
    
    quote_re = re.compile(r'<span class="inq">(.*)</span>')
    
    datalist = []
    for i in range(0,10):
        url = baseurl + str(i * 25)
        html = visit_url(url)

        # 解析数据
        btfsoup = BeautifulSoup(html,"html.parser")
        for item in btfsoup.find_all("p",class_ = "quote"):
            item = str(item)
            quotes = re.findall(quote_re, item)   
            datalist.append(quotes)           

    return datalist

#获取单个指定url网页的内容
def visit_url(url):
    head = {       
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
    }

    request = urllib.request.Request(url,headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)

    return html

#保存数据
def save_to_csv(movies_data, save_path):
    csv_file_name = save_path
    # 使用 'w' 模式打开文件，创建一个 CSV 写入对象
    with open(csv_file_name, 'w', newline='', encoding='utf-8') as csv_file:
        # 创建 CSV 写入器
        csv_writer = csv.writer(csv_file)
        #csv_writer.writerow(['链接','片名','别名','评分','评分人数','影片信息'])
        # 使用 writerow 写入列表中的每一行数据
        for movie_info in movies_data:
            csv_writer.writerow(movie_info)
    print(f"数据已成功写入到 {csv_file_name}")


url = "https://movie.douban.com/top250?start=" # URL
savepath = "豆瓣电影top250.csv" # 保存路径
# 爬取网页
datalist = analyze_html(url)
# 保存数据
save_to_csv(datalist,savepath)
print("爬取完毕")
