import webbrowser
from flask import Flask, render_template, request
import requests
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def proxy(name="index"):
    if request.method == "POST":
        query = request.form["url"]
        res = requests.get(query)
        
        return res.text
    else:
        return render_template("index.html", title=name)


if __name__ == "__main__":
    app.run()
