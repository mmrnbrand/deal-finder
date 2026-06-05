from flask import Flask, render_template, request
from deals import get_deals

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    filtered = get_deals()

    if request.method == "POST":
        keyword = request.form["search"].lower()

        filtered = [
        d for d in get_deals()
        if keyword in d["title"].lower()
    ]

    return render_template("index.html", deals=filtered)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)