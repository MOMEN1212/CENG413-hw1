
import os
from flask import Flask, jsonify

app = Flask(__name__)

APP_NAME = os.getenv("APP_NAME", "CENG413 Homework App")
PORT = int(os.getenv("PORT", "8080"))


@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to my Dockerized application!",
        "application": APP_NAME
    })


@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200


@app.route("/info")
def info():
    return jsonify({
        "application": APP_NAME,
        "port": PORT
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
