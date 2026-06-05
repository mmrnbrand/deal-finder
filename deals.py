import feedparser

SOURCES = [
    "https://slickdeals.net/rss/deals.xml",
    "https://www.dealnews.com/rss/"
]

def get_deals():
    all_deals = []

    for url in SOURCES:
        feed = feedparser.parse(url)

        for entry in feed.entries[:10]:
            all_deals.append({
                "title": entry.title,
                "price": "See deal",
                "link": entry.link
            })

    return all_deals