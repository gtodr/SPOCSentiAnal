# 爬取topicid

import urllib.request, urllib.error
from bs4 import BeautifulSoup    
import re       
import csv

#爬取网页
def analyze_html(baseurl):
    
    # comment_re = re.compile(r'<h3 class="bt ol".*?>(.*?)</h3>')
    
    datalist = []
    url = baseurl
    html = visit_url(url)


    # 解析数据
    btfsoup = BeautifulSoup(html,"html.parser")
    for item in btfsoup.find_all("a"):
        onclick = item.get('onclick')
        if onclick is not None:
            topicid = onclick.split('topicid=')[1].split('&')[0].rstrip('")')
            datalist.append(topicid)   

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
def save_to_csv(data_to_save, save_path):
    csv_file_name = save_path
    # 使用 'w' 模式打开文件，创建一个 CSV 写入对象
    with open(csv_file_name, 'w', newline='', encoding='utf-8') as csv_file:
        # 创建 CSV 写入器
        csv_writer = csv.writer(csv_file)
        #csv_writer.writerow(['链接','片名','别名','评分','评分人数','影片信息'])
        # 使用 writerow 写入列表中的每一行数据
        for info in data_to_save:
            csv_writer.writerow(info)
    print(f"数据已成功写入到 {csv_file_name}")

# 22年
# https://mooc1.wljx.hfut.edu.cn/mooc-ans/course/interactive?courseId=228053910&edit=true&page=1
# 23年
# https://mooc1.wljx.hfut.edu.cn/mooc-ans/course/interactive?courseId=235282766&edit=true&page=1

url = "https://mooc1.wljx.hfut.edu.cn/mooc-ans/course/interactive?courseId=228053910&edit=true&page=1" # URL
# 爬取网页
datalist = analyze_html(url)
# 保存数据
# save_to_csv(datalist,savepath)
with open('./data/topicid_22.txt', 'w', encoding='utf-8') as f:
    # 遍历结果
    for result in datalist:
        # 将结果转换为字符串并写入文件
        f.write(result)
        # 添加一个换行符，使得每个结果都在新的一行
        f.write('\n')

print("爬取完毕")