mecab = MeCab.Tagger("-Owakati")
sentence = "天気がいいから、散歩しましょう"
print(mecab.parse(sentence))