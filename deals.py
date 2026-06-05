import requests

API_URL = "https://www.cheapshark.com/api/1.0/deals?storeID=1&upperPrice=15"

def get_deals():
    try:
        response = requests.get(API_URL, timeout=10)
        data = response.json()

        deals = []

        for item in data[:20]:
            deals.append({
                "title": item["title"],
                "price": f"${item['salePrice']}",
                "link": "https://www.cheapshark.com/redirect?dealID=" + item["cheapestDealID"]
            })

        return deals

    except Exception as e:
        print("API ERROR:", e)
        return []