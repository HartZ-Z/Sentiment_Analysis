import tweepy

from textblob import TextBlob

import matplotlib.pyplot as plt

import time



# Replace with your actual Bearer Token

BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAENR0QEAAAAAc1MLR4UdwwUJkYVIngWdyKAR15E%3DwEZXbQPan91cgycGaOal4vIQH0ysoCMe3EJQjac281VEutlQZ8'



# Initialize Twitter API client with rate limit handling enabled

client = tweepy.Client(bearer_token=BEARER_TOKEN, wait_on_rate_limit=True)



# Function to fetch tweets with retry mechanism

def fetch_tweets(query, max_results=40):

    retries = 0

    while retries < 5:  # Retry up to 5 times

        try:

            response = client.search_recent_tweets(query=query, max_results=max_results, tweet_fields=['text'])

            return response.data

        except tweepy.errors.TooManyRequests as e:

            print(f"Rate limit exceeded. Retrying in {2**retries} seconds...")

            time.sleep(2**retries)  # Exponential backoff

            retries += 1

    print("Failed after multiple retries.")

    return []



# Function to analyse sentiment of tweets

def analyse_sentiment(tweets):

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

    plt.pie(labels, sentiment_counts)

    plt.title('Sentiment Analysis of Tweets')

    plt.ylabel('Number of Tweets')

    plt.show()



if __name__ == "__main__":

    keyword = input("Please enter keyword or hashtag to search: ")

    no_of_tweets = int(input("Please enter how many tweets to analyse: "))



    # Fetch and analyse tweets

    tweets = fetch_tweets(keyword, max_results=no_of_tweets)

    

    if tweets:

        sentiment_counts = analyse_sentiment(tweets)

        print(f"Sentiment counts: Positive: {sentiment_counts[0]}, Negative: {sentiment_counts[1]}, Neutral: {sentiment_counts[2]}")

        

        # Visualize the results

        visualize_results(sentiment_counts)

    else:

        print("No tweets found or an error occurred.")