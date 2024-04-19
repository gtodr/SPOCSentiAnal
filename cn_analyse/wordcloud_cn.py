from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 创建一个词频字典
word_freq = {}

#  从文件读取词频
with open('./data/frequ_output.txt', 'r', encoding='utf-8') as f:
    for line in f:
        word, freq = line.strip().split('\t')
        word_freq[word] = int(freq)

# 创建WordCloud实例
wc = WordCloud(font_path='/System/Library/Fonts/Supplemental/Songti.ttc', background_color='white',  width=1600, height=900)

# 生成词云
wc.generate_from_frequencies(word_freq)
# 保存词云
wc.to_file('./data/wordcloud.png')

# 显示词云
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()