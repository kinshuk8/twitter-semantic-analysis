import json
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter

# Load analyzed tweets
with open("analysis.json", "r", encoding="utf-8") as f:
    tweets = json.load(f)

# Extract sentiments and emotions
sentiments = [tweet["sentiment"] for tweet in tweets]
emotions = [tweet["emotion"] for tweet in tweets]

# Count occurrences
sentiment_counts = Counter(sentiments)
emotion_counts = Counter(emotions)

def plot_pie_chart(data, title, filename):
    plt.figure(figsize=(6, 6))
    plt.pie(data.values(), labels=data.keys(), autopct="%1.1f%%", colors=plt.cm.Paired.colors, startangle=140)
    plt.title(title)
    plt.axis("equal")
    plt.savefig(filename)
    plt.show()

# Generate a word cloud for sentiment analysis
all_text = " ".join(tweet["text"] for tweet in tweets)
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_text)

def plot_wordcloud():
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.title("Most Frequent Words in Tweets")
    plt.savefig("wordcloud.png")
    plt.show()

# Plot Sentiment Pie Chart
plot_pie_chart(sentiment_counts, "Sentiment Distribution", "sentiment_pie.png")

# Plot Emotion Pie Chart
plot_pie_chart(emotion_counts, "Emotion Distribution", "emotion_pie.png")

# Generate and display the word cloud
plot_wordcloud()

print("✅ Pie charts and word cloud saved as 'sentiment_pie.png', 'emotion_pie.png', and 'wordcloud.png'")
