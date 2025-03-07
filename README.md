# Twitter Semantic Analysis and Emotion Detection

This project performs semantic analysis and emotion detection on tweets using NLTK and TextBlob. It fetches tweets based on a specified query, analyzes their sentiment and emotion, and provides visualizations of the results.

## Features

- **Fetch Tweets**: Retrieve tweets based on a search query.
- **Analyze Sentiment**: Determine whether each tweet's sentiment is positive, neutral, or negative.
- **Detect Emotion**: Identify the predominant emotion (e.g., happy, sad, angry, neutral) in each tweet.
- **Visualize Data**: Generate bar charts to visualize sentiment and emotion distributions.

## Prerequisites

- Python 3.x
- Twitter Developer Account with API access
- Libraries: `tweepy`, `nltk`, `textblob`, `matplotlib`, `seaborn`, `python-dotenv`

## Setup Instructions

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/twitter-semantic-analysis.git
   cd twitter-semantic-analysis
   ```

2. **Create a Virtual Environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Twitter API Credentials**:

   - Obtain your API keys and tokens from the [Twitter Developer Portal](https://developer.twitter.com/).
   - Create a `.env` file in the project directory and add your credentials:

     ```
     TWITTER_API_KEY=your_api_key
     TWITTER_API_SECRET_KEY=your_api_secret_key
     TWITTER_ACCESS_TOKEN=your_access_token
     TWITTER_ACCESS_TOKEN_SECRET=your_access_token_secret
     ```

5. **Download NLTK Resources**:

   Run the following commands to download necessary NLTK data:

   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('vader_lexicon')
   ```

## Usage

1. **Fetch Tweets**:

   Modify the `fetch_tweets.py` script to specify your search query and the number of tweets to fetch. Then, run:

   ```bash
   python fetch_tweets.py
   ```

   This will create a `tweets.json` file containing the fetched tweets.

2. **Analyze Tweets**:

   Run the analysis script:

   ```bash
   python analyse.py
   ```

   This will generate an `analysis.json` file with sentiment and emotion annotations for each tweet.

3. **Visualize Results**:

   Generate visualizations by running:

   ```bash
   python visualize.py
   ```

   This will produce bar charts displaying sentiment and emotion distributions.

## 📢 Twitter API Limits
## ⚠️ Free Tier Limitations:

Retrieve: Up to 100 tweets per month
Post: Up to 500 tweets per month

##💡 Upgrading to Basic Tier ($200/month):

Retrieve: Up to 15,000 tweets per month
🔗 More details: Twitter Developer Portal

## Updating the Code for Basic Tier Access

If you upgrade to the Basic Tier, you may need to adjust your code to handle the increased rate limits effectively:

1. **Modify Rate Limit Handling**:

   Update your API initialization in `fetch_tweets.py` to manage rate limits:

   ```python
   import tweepy
   import os
   from dotenv import load_dotenv

   load_dotenv()

   api_key = os.getenv("TWITTER_API_KEY")
   api_secret_key = os.getenv("TWITTER_API_SECRET_KEY")
   access_token = os.getenv("TWITTER_ACCESS_TOKEN")
   access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

   auth = tweepy.OAuthHandler(api_key, api_secret_key)
   auth.set_access_token(access_token, access_token_secret)

   api = tweepy.API(auth, wait_on_rate_limit=True)
   ```

   Setting `wait_on_rate_limit=True` ensures that your application waits and resumes fetching data when the rate limit resets.

2. **Implement Pagination**:

   To retrieve a large number of tweets, implement pagination using Tweepy's `Cursor`:

   ```python
   import tweepy
   import json

   def fetch_tweets(query, count):
       tweets = []
       for tweet in tweepy.Cursor(api.search_tweets, q=query, lang="en", tweet_mode="extended").items(count):
           tweets.append(tweet._json)
       return tweets

   if __name__ == "__main__":
       query = "your search query"
       count = 100  # Number of tweets to fetch
       fetched_tweets = fetch_tweets(query, count)
       with open("tweets.json", "w", encoding="utf-8") as f:
           json.dump(fetched_tweets, f, ensure_ascii=False, indent=4)
   ```

   Adjust the `count` variable based on your requirements and ensure it aligns with your current rate limits.

3. **Monitor Rate Limits**:

   Regularly monitor your application's rate limit status to avoid exceeding the allocated limits. You can check your rate limit status using:

   ```python
   rate_limit_status = api.rate_limit_status()
   print(json.dumps(rate_limit_status, indent=4))
   ```

   This will provide insights into your current usage and remaining quota.

By following these steps, you can effectively utilize the Basic Tier's capabilities while adhering to Twitter's rate limits.

---

*Note*: Always ensure compliance with Twitter's Developer Agreement and Policy when using the API. 
