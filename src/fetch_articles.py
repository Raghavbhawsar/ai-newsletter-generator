import feedparser, json, pandas as pd
from datetime import datetime

def load_feeds():
    with open("data/feeds.json", "r") as f:
        return json.load(f)

def fetch_articles():
    feeds = load_feeds()
    articles = []
    for source, url in feeds.items():
        try:
            feed = feedparser.parse(url)
            for entry in feed.entries:
                articles.append({
                    "source": source,
                    "title": entry.get("title", ""),
                    "link": entry.get("link", ""),
                    "summary": entry.get("summary", ""),
                    "published": entry.get("published", ""),
                    "fetched_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                })
        except Exception as e:
            print(f"Error fetching {source}: {e}")
    pd.DataFrame(articles).to_csv("data/articles.csv", index=False)
    return articles

if __name__ == "__main__":
    fetch_articles()
