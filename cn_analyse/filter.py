#数据初步清洗 筛选出其中字数大于4的句子
import re

# 定义正则表达式模式来匹配日语和中文部分
lang_pattern = re.compile(r'[\u4e00-\u9fa5\u3040-\u309F\u30A0-\u30FF\uFF66-\uFF9F]+')  # 匹配中文和日语

# 聊天记录文件
data_file = "./data/comments_cn_raw.txt"

# 读取文本
with open(data_file, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 存储中文和日语部分的列表
comment_lines = []

# 提取中文和日语部分，保持原始文本格式
for line in lines:
    sentences = lang_pattern.findall(line)
    #筛选出其中字数大于4的句子
    filtered_sentences = [sentence for sentence in sentences if len(sentence) >= 4]
    text = ' '.join(filtered_sentences)
    if text.strip():
        if any(char >= '\u4e00' and char <= '\u9fff' for char in text):  # 判断是否包含中文字符
            comment_lines.append(text.strip() + '\n')

# 将提取的中日文部分写入文件
with open('./data/filtered_data.txt', 'w', encoding='utf-8') as file:
    file.writelines(comment_lines)
