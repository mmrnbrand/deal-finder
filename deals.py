import feedparser

FEEDS = [
    "https://www.dealnews.com/rss/",
    "https://www.cheapshark.com/feeds/deals?storeID=1"
]

def get_deals():
    all_deals = []

    for url in FEEDS:
        feed = feedparser.parse(url)

        for entry in feed.entries[:10]:
            all_deals.append({
                "title": entry.title,
                "price": "Deal",
                "link": entry.link
            })

    return all_deals