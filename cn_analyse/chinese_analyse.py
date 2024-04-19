#中文情感分析系统


from snownlp import SnowNLP

# 消极的评论列表
negativeList = []
# 积极的评论列表
positiveList = []

# 打开文本
with open("chinese.txt", "r", encoding="utf-8") as file:
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

print('积极的评论有：%d条，消极的评论有：%d条'% (len(positiveList), len(negativeList)))
print("积极的评论为：")
for i in positiveList:
    print(i)
print("\n\n\n消极的评论为：")
for i in negativeList:
    print(i)