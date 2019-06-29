# !/usr/bin/env python3

"""
This file starts the web server.
"""
import os

from flask import Flask, jsonify, render_template

from twitter_fire_scraper.config import Config
from twitter_fire_scraper.scraper import Scraper
from twitter_fire_scraper.twitter import TwitterAuthentication

current_folder = os.path.abspath(os.path.dirname(__file__))
static_folder = os.path.join(current_folder, 'static')
template_folder = os.path.join(current_folder, 'templates')

app = Flask(__name__, static_url_path='/static', template_folder=template_folder, static_folder=static_folder)

app.debug = True

scraper = Scraper(twitter_authentication=TwitterAuthentication.autodetect_twitter_auth())


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":

    if app.debug:
        app.config.update({
            "EXPLAIN_TEMPLATE_LOADING": True,
        })

    app.run(host="127.0.0.1", port=Config.Defaults.WEB_PORT)
