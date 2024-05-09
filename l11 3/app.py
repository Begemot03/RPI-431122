from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("pages/index.html")

@app.route("/offer")
def offer():
    return render_template("pages/offer.html")

@app.route("/work")
def work():
    return render_template("pages/work.html")