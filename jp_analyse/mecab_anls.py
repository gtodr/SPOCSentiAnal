import MeCab
mecab = MeCab.Tagger('-r/dev/null -d/usr/local/etc/mecabrc')
sentence = "天気がいいから、散歩しましょう"
print(mecab.parse(sentence))