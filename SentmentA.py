import textblob._text
import textblob.sentiments
import tweepy
import textblob
import tweepy.auth
import tweepy.cursor


#consumer_key = "noEolsdnyWvv3HleJGWAeUATv" 
#consumer_key_secret = "1GNeL0lzFGDXTetT2Q9dA8DpkTRoqUYVky1S8GRO0XgYJlD6qp" 
#access_key = "1642610233024614400-V6PDQ6CybrCkZSPqaonMQoTtoMjgpY" 
#access_key_secret = "yJSWKbHsXYvBDarmyt5fQwnUV5w6YN4jiiZnfb5kus5nX" 

#auth = tweepy.OAuthHandler(consumer_key , consumer_key_secret )
#auth.set_access_token(access_key , access_key_secret)
client = tweepy.Client(
  consumer_key = "EKCg7mEXpjztZ4bMTfLj2lTBx" ,
  consumer_secret = "XzjFFfuQpN9npmshKPvobcQ2hY1M6UIyvAxSXW0Pg6f1C4qRc0" ,
  access_token = "1856342846418120704-5X7SwhyJs70GrI7TJ4hJ2FSwvhVdxn" ,
  access_token_secret = "g0xOL6cwSwebxzhhDECr9LOZqhzV2FpApyCK7wBJxHqsN",
  bearer_token="AAAAAAAAAAAAAAAAAAAAAIJo0QEAAAAAprq4iPqxUHyrGFM02cZ5xKyCyLQ%3DF7ZnOyORwtBlvx60ZCkigZ3XQCsLYqOpZZ1fbzeij8Wo79ZkXt",
)
    

keyword = input("Enter the topic you are interesed in : ")
no_of_searches = int(input("Enter how many tweets you want to search: "))



tweets = client.search_recent_tweets(query=keyword, max_results=no_of_searches)

positive = 0
negative = 0
Neutral = 0
polarity = 0

for tweet in tweets :
  print(textblob._text)



  