import feedparser

SLICKDEALS_RSS = "https://slickdeals.net/newsearch.php?mode=rss"

def get_deals():
    feed = feedparser.parse(SLICKDEALS_RSS)

    deals = []

    for entry in feed.entries[:20]:
        deals.append({
            "title": entry.title,
            "price": "Deal",
            "link": entry.link
        })

    return deals