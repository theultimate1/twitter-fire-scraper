import os
from flask import Flask, request, render_template, jsonify, url_for

from config import Config
from twitter import TwitterClient
from util import strtobool

flask_app = Flask(__name__, static_path="/static")
twitter_api = TwitterClient()


@flask_app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    flask_app.run(host="127.0.0.1", port=port, debug=True)
