from flask import Flask, request, jsonify
import tweepy
from textblob import TextBlob
import time

app = Flask(__name__)

BEARER_TOKEN = 'Your Bearer Key'
client = tweepy.Client(bearer_token=BEARER_TOKEN, wait_on_rate_limit=True)

def fetch_tweets(query, max_results=40):
    try:
        response = client.search_recent_tweets(query=query, max_results=max_results, tweet_fields=['text'])
        return [tweet.text for tweet in response.data] if response.data else []
    except Exception as e:
        return str(e)

def analyse_sentiment(tweets):
    positive = negative = neutral = 0

    for tweet in tweets:
        analysis = TextBlob(tweet)
        if analysis.sentiment.polarity > 0:
            positive += 1
        elif analysis.sentiment.polarity < 0:
            negative += 1
        else:
            neutral += 1

    return {"positive": positive, "negative": negative, "neutral": neutral}

@app.route('/analyze', methods=['GET'])
def analyze():
    keyword = request.args.get('keyword')
    no_of_tweets = int(request.args.get('count', 10))

    tweets = fetch_tweets(keyword, max_results=no_of_tweets)
    if tweets:
        sentiment_counts = analyse_sentiment(tweets)
        return jsonify(sentiment_counts)
    return jsonify({"error": "No tweets found"})

if __name__ == '__main__':
    app.run(debug=True)
