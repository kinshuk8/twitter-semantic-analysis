import os
from dotenv import load_dotenv

import tweepy
import json
import time
from config import TWITTER_API_KEY, TWITTER_API_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET

load_dotenv()

TWITTER_BEARER_KEY = os.getenv("TWITTER_BEARER_KEY")

# Authenticate using Twitter API v2
client = tweepy.Client(bearer_token=TWITTER_BEARER_KEY)

# Function to fetch tweets (v2 API)
def fetch_tweets(query, count=50):
    try:
        tweets = []
        response = client.search_recent_tweets(query=query, max_results=min(count, 100), tweet_fields=["created_at", "text"])
        
        if response.data:
            for tweet in response.data:
                tweets.append({"id": tweet.id, "text": tweet.text, "created_at": tweet.created_at.isoformat()})

        # Save to JSON
        with open("tweets.json", "w", encoding="utf-8") as f:
            json.dump(tweets, f, indent=4)

        print(f"✅ Successfully fetched {len(tweets)} tweets.")

    except tweepy.TooManyRequests:
        print("⚠ Twitter rate limit exceeded! Waiting before retrying...")
        time.sleep(900)  # Wait for 15 minutes
        fetch_tweets(query, count)  # Retry fetching

# Run the function
if __name__ == "__main__":
    fetch_tweets("machine learning", 50)
