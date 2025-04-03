# Sentiment Analysis using Twitter API

## Overview
This project analyzes the sentiment of tweets based on a given keyword or hashtag. It utilizes the Twitter API to fetch recent tweets and uses TextBlob for sentiment analysis. The project includes:

1. **Sentiment_Analysis.py** - A script that fetches tweets, analyzes sentiment, and visualizes the results using Matplotlib.
2. **Sentiment_API.py** - A Flask-based API that returns sentiment analysis results in JSON format.

---

## Installation and Setup

### Prerequisites
Ensure you have Python installed (preferably Python 3.7+).

Install the required dependencies using:
```bash
pip install tweepy textblob flask matplotlib
```

### Twitter API Authentication
Replace the `BEARER_TOKEN` in both files with your own Twitter API Bearer Token.

---

## How to Use

### 1. Running Sentiment_Analysis.py (Standalone Script)
Execute the script from the command line:
```bash
python Sentiment_Analysis.py
```
- Enter a keyword or hashtag to search.
- Enter the number of tweets to analyze.
- The script will fetch tweets, analyze sentiment, and display a bar chart visualization.

---

### 2. Running Sentiment_API.py (Flask API)
Start the Flask server using:
```bash
python Sentiment_API.py
```
Once running, you can analyze tweets via an API request:
```bash
http://127.0.0.1:5000/analyze?keyword=example&count=50
```
This will return a JSON response with sentiment counts.

---

## Example API Response
```json
{
    "positive": 12,
    "negative": 8,
    "neutral": 30
}
```

---

## Notes
- Ensure you have valid Twitter API credentials.
- The script implements rate-limit handling to avoid API restrictions.
- The Flask API can be extended for deployment on cloud services like AWS, Heroku, or Render.

---

## License
This project is open-source. Feel free to modify and distribute.

---

## Author And GitHub Handles ( Team )
Eda Mone (Mohammad Taufiq ( HartZ-Z ) , Harshwardhan Sharma ( Harshwardhan1276 ) , Nikunj Pareek ( NikunjPareek ))





