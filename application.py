import requests
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/convert", methods=["POST"])
def convert():
    # Query for currency exchange rate
    currency = request.form.get("currency")
    res = requests.get("http://api.fixer.io/latest", params={"base":"USD", "symbols":currency})
    # Check request as if suceeded
    if res.status_code != 200:
        return jsonify({"success": False})
    data = res.json()
    # Check the currency is in reponse
    if currency not in data["rates"]:
        return jsonify({"success": False})
    return jsonify({"success": True, "rate":data["rates"][currency]})
# Tip to run server from cmd"
# set FLASK_APP=application.py
# flask run --host=0.0.0.0 --port=3000
