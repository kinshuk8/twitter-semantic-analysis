import json
import nltk
from textblob import TextBlob

# Load Emotion Lexicon (Example)
emotion_dict = {
    "happy": ["joy", "excited", "pleased", "amazing", "great"],
    "sad": ["unhappy", "miserable", "depressed", "upset"],
    "angry": ["furious", "annoyed", "irritated", "mad"]
}

# Function to detect emotions
def detect_emotion(text):
    words = nltk.word_tokenize(text.lower())
    for emotion, keywords in emotion_dict.items():
        if any(word in words for word in keywords):
            return emotion
    return "neutral"

# Function to analyze sentiment and emotion
def analyze_tweets():
    with open("tweets.json", "r", encoding="utf-8") as f:
        tweets = json.load(f)

    results = []
    for tweet in tweets:
        analysis = TextBlob(tweet["text"])
        sentiment = "positive" if analysis.sentiment.polarity > 0 else "negative" if analysis.sentiment.polarity < 0 else "neutral"
        emotion = detect_emotion(tweet["text"])

        results.append({
            "id": tweet["id"],
            "text": tweet["text"],
            "sentiment": sentiment,
            "emotion": emotion
        })

    # Save to JSON
    with open("analysis.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4)

    print("✅ Sentiment and emotion analysis completed!")

# Run analysis
if __name__ == "__main__":
    nltk.download("punkt")
    analyze_tweets()
