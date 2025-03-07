import json
import matplotlib.pyplot as plt
import seaborn as sns
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

# Define function for plotting
def plot_distribution(data, title, xlabel, ylabel, filename):
    plt.figure(figsize=(8, 5))
    sns.barplot(x=list(data.keys()), y=list(data.values()), palette="viridis")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.savefig(filename)  # Save the plot as an image
    plt.show()

# Plot Sentiment Distribution
plot_distribution(sentiment_counts, "Sentiment Distribution", "Sentiment", "Count", "sentiment_plot.png")

# Plot Emotion Distribution
plot_distribution(emotion_counts, "Emotion Distribution", "Emotion", "Count", "emotion_plot.png")

print("✅ Visualizations saved as 'sentiment_plot.png' and 'emotion_plot.png'")
