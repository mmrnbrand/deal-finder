from flask import Flask, render_template, request
from deals import get_deals
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    all_deals = get_deals()
    filtered = all_deals

    if request.method == "POST":
        keyword = request.form["search"].lower().strip()

        filtered = [
            d for d in all_deals
            if keyword in d["title"].lower()
        ]

    return render_template("index.html", deals=filtered)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)