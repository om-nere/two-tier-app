from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route("/")
def home():
    return "Two Tier App is Running with Docker & Jenkins 🚀"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
