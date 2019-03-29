from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__, static_url_path="/static")

app.config['MONGO_DBNAME'] = 'twitterfirescraperapi'  # name of your cluster
app.config['MONGO_URI'] = 'mongodb+srv://trungpham10:!twitterfire1@twitterfirescraperapi-i6mwc.mongodb.net/test?retryWrites=true'
# mongodb username and password here

mongo = PyMongo(app)
