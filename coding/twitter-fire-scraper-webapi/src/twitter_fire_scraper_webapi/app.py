import os
from flask import Flask, request, render_template, jsonify, url_for, abort, Response


app = Flask(__name__, static_url_path="/static")


@app.route('/scrape_terms', methods=['GET'])
def scrape_terms():

    count = request.args.get("count")

    if not count:
        abort(400, "'count' is a required URL parameter!")

    return jsonify("You want {} tweets?".format(count))

@app.route('/scrape_accounts', methods=['GET'])
def scrape_accounts():

    count = request.args.get("count")

    if not count:
        abort(400, "'count' is a required URL parameter!")

    return jsonify("You want {} tweets for {}?".format(count, term))

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
    port = int(os.environ.get('PORT', 3620))

    app.run(host="127.0.0.1", port=port, debug=True)
