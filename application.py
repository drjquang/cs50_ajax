from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# Tip to run server from cmd
# set FLASK_APP=application.py
# flask run --host=0.0.0.0 --port=3000
