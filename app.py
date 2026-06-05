from flask import Flask, render_template
from deals import get_deals
import os

app = Flask(__name__)

print("🔥 APP IS RUNNING - NEW CODE DEPLOYED")

@app.route("/")
def home():

    deals = get_deals()

    print("🔥 RAW DEAL SAMPLE:", deals[:1])

    return str(deals[:3])

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)