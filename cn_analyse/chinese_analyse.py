#中文情感分析系统
from snownlp import SnowNLP
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 消极的评论列表
negativeList = []
# 积极的评论列表
positiveList = []

# 打开文本
with open("./data/comments_cn.txt", "r", encoding="utf-8") as file:
    text = file.read()
    # 使用 split() 方法按换行符分割文本
    commentList = text.split("\n")

# 循环分析
for comment in commentList:
    # 去除首尾空白字符，如果评论为空则跳过
    comment = comment.strip()
    if comment:
        s = SnowNLP(comment)
        # 获取情感分数
        sentiment_score = s.sentiments
        if sentiment_score < 0.5:
            # 说明是负面评论
            negativeList.append(comment)
        else:
            # 说明是积极评论
            positiveList.append(comment)

# 积极评论条数
pos_comments = len(positiveList)
# 消极评论条数
neg_comments = len(negativeList)
print('积极的评论有：%d条，消极的评论有：%d条'% (pos_comments, neg_comments))
# print("积极的评论为：")
# for i in positiveList:
#     print(i)
# print("\n\n\n消极的评论为：")
# for i in negativeList:
#     print(i)

# 根据评论的数量，计算积极评论和消极评论的比例
# 评论总数
total_comments = pos_comments + neg_comments
# 积极评论比例
pos_ratio = pos_comments / total_comments
# 消极评论比例
neg_ratio = neg_comments / total_comments

# 设置字体为中文字体
font = FontProperties(fname='/System/Library/Fonts/Supplemental/Songti.ttc')
# 绘制图表
plt.figure(figsize=(6, 6))
labels = ['积极', '消极']
sizes = [pos_ratio, neg_ratio]
colors = ['green', 'red']
explode = (0, 0.1)
patches, l_text, p_text = plt.pie(sizes, explode=explode, labels=labels, colors=colors, labeldistance=1.1, autopct='%2.0f%%', shadow=False, startangle=90, pctdistance=0.6)
for t in l_text:
    t.set_fontproperties(font)
for t in p_text:
    t.set_fontproperties(font)
plt.axis('equal')
plt.legend(prop=font)
plt.title('中文评论比例', fontproperties=font)
plt.show()