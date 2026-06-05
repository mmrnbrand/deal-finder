import requests

API_URL = "https://www.cheapshark.com/api/1.0/deals?storeID=1&upperPrice=15"

def get_deals():
    try:
        r = requests.get(API_URL, timeout=10)
        print("STATUS:", r.status_code)

        data = r.json()
        print("ITEMS:", len(data))

        deals = []

        for item in data[:20]:
            deals.append({
                "title": item.get("title", "No title"),
                "price": item.get("salePrice", "N/A"),
                "link": "https://www.cheapshark.com/redirect?dealID=" + item.get("dealID", "")
            })

        return deals

    except Exception as e:
        print("ERROR:", str(e))
        return []