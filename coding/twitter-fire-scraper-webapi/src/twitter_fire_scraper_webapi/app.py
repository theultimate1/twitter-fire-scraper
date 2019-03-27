import os
from flask import Flask, request, render_template, jsonify, url_for, abort, Response

import twitter_fire_scraper

import twitter_fire_scraper
from twitter_fire_scraper.scraper import Scraper
from twitter_fire_scraper.twitter import TwitterAuthentication
from twitter_fire_scraper.util import jsonify_status_dict

app = Flask(__name__, static_url_path="/static")
scraper = Scraper(twitter_authentication=TwitterAuthentication.autodetect_twitter_auth())

@app.route('/scrape_terms', methods=['GET'])
def scrape_terms():

    count = request.args.get("count")
    if not count:
        abort(400, "'count' is a required URL parameter!")

    try:
        count = int(count)

        if count < 0:
            raise ValueError
    except ValueError:
        abort(400, "'count' should be a valid number!")

    terms = request.args.get("terms")

    if not terms:
        abort(400, "'terms' is a required URL parameter!")

    terms = terms.split(",")
    if len(terms) <= 0:
        abort(400, "'terms' cannot be an empty list!")

    geocode = request.args.get("geocode")

    results = (scraper.scrape_terms(terms=terms, count=count, geocode=geocode)) # dict object

    results = jsonify_status_dict(results)  # json object

    return jsonify(results)
    # return jsonify("You want {} tweets for {}?".format(count, terms))


@app.route('/scrape_accounts', methods=['GET'])
def scrape_accounts():

    count = request.args.get("count")
    accounts = request.args.get("accounts")
    accounts = accounts.split(",")

    if not count:
        abort(400, "'count' is a required URL parameter!")

    if not accounts:
        abort(400, "'accounts' is a required URL parameter!")

    results = (scraper.scrape_accounts(accounts=accounts, count=count))

    results = jsonify_status_dict(results)

    return jsonify(results)
    # return jsonify("You want {} tweets for {}?".format(count, term))


@app.route('/scrape', methods=['GET'])
def scrape():
    count = request.args.get("count")
    if not count:
        abort(400, "'count' is a required URL parameter!")
    try:
        count = int(count)
        if count < 0:
            raise ValueError
    except ValueError:
        abort(400, "'count' should be a valid number!")

    terms = request.args.get("terms")
    if not terms:
        abort(400, "'terms' is a required URL parameter!")
    terms = terms.split(",")
    if len(terms) <= 0:
        abort(400, "'terms' cannot be an empty list!")

    accounts = request.args.get("accounts")
    if not accounts:
        abort(400, "'accounts' is a required URL parameter!")
    accounts = accounts.split(",")
    if len(accounts) <= 0:
        abort(400, "'accounts' cannot be an empty list!")

    geocode = request.args.get("geocode")

    results = (scraper.scrape(terms=terms, accounts=accounts, count=count, geocode=geocode))

    results = jsonify_status_dict(results)

    return jsonify(results)
    # return jsonify("You want {} tweets for {}?".format(count, term))


@app.route('/info', methods=['GET'])
def info(): # function: check webapi is running or not
    return "twitter-fire-scraper-webapi"

@app.route('/')
def index():
    return jsonify({'json': 'hacked'})

@app.route('/add/<int:x>/<int:y>', methods=['GET'])
def add_numbers(x, y):
    return str(x+y)

### Task to be completed:
# https://github.com/raaraa/IPRO497-Analytics-Team/tree/master/Documents/spring-break-tasks

if __name__ == "__main__":
    port = 3620

    app.run(host="127.0.0.1", port=port, debug=True)
