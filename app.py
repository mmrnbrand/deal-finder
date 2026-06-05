from flask import Flask, render_template
from deals import get_deals
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():

    deals = get_deals()

    print("DEALS COUNT:", len(deals))  # check logs

    return render_template("index.html", deals=deals)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)