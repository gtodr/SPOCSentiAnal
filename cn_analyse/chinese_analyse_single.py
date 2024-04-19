#中文情感分析系统（单句查看）


from snownlp import SnowNLP

x=1
print("输入0终止程序")
while(x!=0):
    comment = input("请输入待测试评论\n")
    if comment=='0':
        break
    s = SnowNLP(comment)
    # 获取情感分数
    sentiment_score = s.sentiments
    if sentiment_score < 0.5:
        # 说明是负面评论
        print("该评论为负面\n")
    else:
        # 说明是积极评论
        print("该评论为正面\n")