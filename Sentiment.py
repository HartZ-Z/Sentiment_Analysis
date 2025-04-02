import tweepy
from textblob import TextBlob
import matplotlib.pyplot as plt

# Twitter API v2 credentials
BEARER_TOKEN = 'YOUR_BEARER_TOKEN_HERE'

# Initialize Twitter API client
client = tweepy.Client(bearer_token=BEARER_TOKEN)

# Function to fetch tweets without waiting for rate limit reset
def fetch_tweets(query, max_results=100):
    try:
        response = client.search_recent_tweets(query=query, max_results=max_results, tweet_fields=['text'])
        return response.data
    except tweepy.errors.TooManyRequests as e:
        print("Rate limit exceeded. Unable to fetch more tweets.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Function to analyze sentiment of tweets
def analyze_sentiment(tweets):
    positive = negative = neutral = 0

    for tweet in tweets:
        analysis = TextBlob(tweet.text)
        if analysis.sentiment.polarity > 0:
            positive += 1
        elif analysis.sentiment.polarity < 0:
            negative += 1
        else:
            neutral += 1

    return positive, negative, neutral

# Function to visualize results
def visualize_results(sentiment_counts):
    labels = ['Positive', 'Negative', 'Neutral']
    plt.bar(labels, sentiment_counts)
    plt.title('Sentiment Analysis of Tweets')
    plt.ylabel('Number of Tweets')
    plt.show()

if __name__ == "__main__":
    keyword = input("Please enter keyword or hashtag to search: ")
    no_of_tweets = int(input("Please enter how many tweets to analyze: "))

    # Fetch and analyze tweets
    tweets = fetch_tweets(keyword, max_results=no_of_tweets)

    if tweets:
        sentiment_counts = analyze_sentiment(tweets)
        print(f"Sentiment counts: Positive: {sentiment_counts[0]}, Negative: {sentiment_counts[1]}, Neutral: {sentiment_counts[2]}")

        # Visualize the results
        visualize_results(sentiment_counts)
    else:
        print("No tweets found or an error occurred.")
