#日语情感分析

from asari.api import Sonar
sonar = Sonar()
# 消极的评论列表
negativeList = []
# 积极的评论列表
positiveList = []
# 打开文本
with open("comments.txt", "r", encoding="utf-8") as file:
    text = file.read()
    # 使用 split() 方法按换行符分割文本
    commentList = text.split("\n")
# 循环分析
for comment in commentList:
    result = sonar.ping(text=comment)
    if result['top_class']=='negative':
        # 说明是负面评论
        negativeList.append(result)
    else:
        # 说明是积极评论
        positiveList.append(result)
print('积极的评论有：%d条，消极的评论有：%d条'% (len(positiveList), len(negativeList)))
# print(negativeList)