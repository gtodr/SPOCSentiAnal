import jieba.posseg as pseg
from collections import Counter

# 从文件读取评论
comments = []  # 评论列表
stop_words = []  # 停用词列表
with open('./data/comments_cn.txt', 'r', encoding='utf-8') as f:
    for line in f:
        comments.append(line.strip())
# 读取停用词
with open('./data/stop_words.txt', 'r', encoding='utf-8') as f:
    stop_words = [line.strip() for line in f]

# 分词
words = []
for comment in comments:
    words.extend([(x.word, x.flag) for x in pseg.lcut(comment)])

# 过滤出名词和动词
noun_verb = [word for word, flag in words if flag.startswith('n') or flag.startswith('v')]
# 过滤停用词
noun_verb = [word for word in noun_verb if word not in stop_words]

# 统计频率
counter = Counter(noun_verb)
# print(counter)

# 将统计结果写入文件
with open('./data/frequ_output.txt', 'w', encoding='utf-8') as f:
    for word, count in counter.most_common():
        f.write(f'{word}\t{count}\n')