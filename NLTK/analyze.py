import nltk
from nltk.sentiment import SentimentIntensityAnalyzer


# error: 找不到nltk_data，得修改nltk environment variable路径

def analyze_sentiment(text):
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = sid.polarity_scores(text)
    if sentiment_scores['compound'] >= 0.05:
        return "Positive"
    elif sentiment_scores['compound'] <= -0.05:
        return "Negative"
    else:
        return "Neutral"

# 示例用法
text = "I love this movie! It's amazing!"
sentiment = analyze_sentiment(text)
print(sentiment)