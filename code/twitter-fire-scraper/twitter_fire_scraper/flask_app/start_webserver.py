# !/usr/bin/env python3

"""
This file starts the web server.
"""
import os

from flask import Flask, jsonify, render_template, redirect

from twitter_fire_scraper.flask_app.forms import ScrapeTermForm
from twitter_fire_scraper.config import Config, FlaskConfig
from twitter_fire_scraper.scraper import Scraper
from twitter_fire_scraper.twitter import TwitterAuthentication

current_folder = os.path.abspath(os.path.dirname(__file__))
static_folder = os.path.join(current_folder, 'static')
template_folder = os.path.join(current_folder, 'templates')

app = Flask(__name__, static_url_path='/static', template_folder=template_folder, static_folder=static_folder)

app.debug = FlaskConfig.DEBUG

scraper = Scraper(twitter_authentication=TwitterAuthentication.autodetect_twitter_auth())


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/success")
def success():
    return "Whatever you just tried worked. Congrats :)"


@app.route('/scrape_term', methods=("GET", "POST"))
def scrape_term():
    form = ScrapeTermForm()

    tweets = None

    if form.validate_on_submit():
        tweets = scraper.scrape_terms(terms={form.term.data}, count=form.amount.data)

    return render_template('scrape.html', form=form, tweets=tweets)


if __name__ == "__main__":

    app_kwargs = {
        "host": "127.0.0.1",
        "port": FlaskConfig.WEB_PORT,
    }

    if FlaskConfig.DEBUG:

        # Verbose template loading.
        app.config.update({
            "EXPLAIN_TEMPLATE_LOADING": True,
        })

        # Use ad-hoc SSL.
        # This prevents us from having to create an SSL cert in development but still encrypts the connection.
        app_kwargs.update({
            "ssl_context": "adhoc",
        })

    else:  # Not debug mode, production mode.

        # Use SSL cert + key loaded from a file.
        app_kwargs.update({
            "ssl_context": (FlaskConfig.SSL_CERTIFICATE_PATH, FlaskConfig.SSL_KEY_PATH),
        })

    # Update app's config no matter what.
    app.config.update({
        'SECRET_KEY': FlaskConfig.SECRET_KEY,
    })

    app.run(**app_kwargs)
