# 非登陆状态爬取评论

import urllib.request, urllib.error
from bs4 import BeautifulSoup    
import re       
import csv

#<h3 class="bt ol" id="replyfirstname_1512107927" name="replyfirstname">分からない<br>老人のための専門的な人や法律がある</h3>

#读取topic id
def read_topicid(file_name='topicid.txt'):
    with open(file_name, 'r') as f:
        # 读取文件中的所有行
        lines = f.readlines()
    return lines

#爬取网页
def analyze_html(baseurl, topicids):
    
    # comment_re = re.compile(r'<h3 class="bt ol".*?>(.*?)</h3>')
    datalist = []

    for line in topicids:
        data = []
        url = baseurl + line
        html = visit_url(url)
        # 解析数据
        btfsoup = BeautifulSoup(html,"html.parser")
        for item in btfsoup.find_all("h3", attrs={'class':"bt ol", 'name':'replyfirstname'}):
            # item = str(item)
            item = item.get_text()
            # comment = re.findall(comment_re, item)   
            # datalist.append(comment)  
            data.append(item) 

        datalist.append(data)        

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


# base url
    # 23
    # https://mooc1.wljx.hfut.edu.cn/sliver/bbs/gettopicdetail?courseId=235282766&clazzid=78388241&topicid=
# 22
    # https://mooc1.wljx.hfut.edu.cn/sliver/bbs/gettopicdetail?courseId=228053910&clazzid=62217808&topicid=
# 对应课程的base url
url = "https://mooc1.wljx.hfut.edu.cn/sliver/bbs/gettopicdetail?courseId=235282766&clazzid=78388241&topicid=" # URL
# 保存路径
savepath = "./data/comments.txt" 
# 对应年份topicid保存路径
topicid_savepath = "./data/topicid_23.txt"
# 读取topicid
topicids = read_topicid(topicid_savepath)
# 爬取网页
datalist = analyze_html(url, topicids)
# 保存数据
# save_to_csv(datalist,savepath)
with open(savepath, 'w', encoding='utf-8') as f:
    # 遍历结果
    for result in datalist:
        # 将结果转换为字符串并写入文件
        for comment in result:
            f.write(comment)
            # 添加一个换行符，使得每个结果都在新的一行
            f.write('\n')

print("爬取完毕")