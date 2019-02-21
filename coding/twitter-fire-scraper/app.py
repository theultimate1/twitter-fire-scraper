import os
from flask import Flask, request, render_template, jsonify, url_for

from config import Config
from twitter import TwitterClient
from util import strtobool

app = Flask(__name__, static_path="/static")
twitter_api = TwitterClient()


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host="127.0.0.1", port=port, debug=True)
