import feedparser

google_news_url = "https://news.google.com/news/rss"

def get_headlines(rss_url):
    feed = feedparser.parse(rss_url)
    return [entry.title for entry in feed.entries]

print(get_headlines(google_news_url))