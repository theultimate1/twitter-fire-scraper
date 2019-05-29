[![PyPI version](https://badge.fury.io/py/twitter-fire-scraper.svg)](https://badge.fury.io/py/twitter-fire-scraper)

# What is this?

This is a Python Twitter "Fire event" scraper/listener.

It is an application that will listen for or scrape data relating to house fires (Chicago specifically) in order to analyze how people use Twitter as a platform to report and talk about disasters.

# How will this use Twitter data?

This application allows one to analyze, collect, and collate data about house fires and other disasters on Twitter.

# How do I install this?

## Dependencies

- [Python 3 or greater](https://www.python.org/downloads/)
- [MongoDB](https://www.mongodb.com/)

## Steps

```
pip install twitter-fire-scraper
```

If it is already installed and a newer version is available, you can update with:

```
pip install twitter-fire-scraper --upgrade
```

## Notes

This README assumes all commands take place in the same folder as this README file.

## Examples

Examples of how to use this package can be found in [this examples folder](python_example_code) and also in [our internal test suites](src/twitter_fire_scraper/tests).

 These should give you a good idea of how to use our scraper, and can be considered a 'living standard' of how our code works.

<!-- TODO write a wiki!!! -->

 ## Setting up your secrets

This secrets file is only used for the demos. When using this library, it is up to you to manage how you store and retrieve your API keys.

More specifically, if the `Scraper` object is not initialized with a `TwitterAuthentication` object, it will search for a file called `~/secrets.json` for API keys as a fallback.

This is to make the demonstrations work and not recommended usage when using the library.

A note: These are called 'secrets' for a reason. Don't ever stage or commit `secrets.json`, please.

### Twitter secrets

You will need:

- A twitter developer account & API key

  - A consumer API key (goes into `"consumer_key"`)
  - A consumer API secret key (goes into `"consumer_secret"`)
  - An access token (goes into `"access_token"`)
  - An access secret (goes into `"access_token_secret"`)

- A twitter handle you're authorized to make queries on behalf of

You are to put these into a file called `secrets.json` in your home folder under `.twitterfirescraper/` (For example, mine is `C:/Users/henryfbp/.twitterfirescraper/secrets.json`.)

An example file is provided for you to base your file off of, called `secrets.example.json`.

### MongoDB secrets

The demos in our code connect to the following mongodb address:

```
mongodb://localhost:27017/
```

## Setting up a database

For the database, we have chosen to use MongoDB since twitter data is stored in JSON and MongoDB is very well-suited for storing JSON data.

Follow [this tutorial](https://docs.mongodb.com/v3.2/tutorial/) on how to install MongoDB.

## Developer dependencies

- Same as above.
- [Ruby](https://www.ruby-lang.org/en/), used for running scripts to build and test Python wheels.

### Setting up Pipenv

You can install Pipenv by executing

```
pip install pipenv
```

You can then install all packages (including dev packages like `twisted`) in this folder's `./Pipenv` by executing

```
pipenv install --dev
```

Then, you can run tests by executing

```
pipenv run python /src/twitter-fire-scraper/tests/test/__main__.py
```

## Running a functional demo

Inside this folder, there are two files called `Run-Demo.bat` and `Run-Demo.ps1`. You can run either of those to start a demo intended for presentation purposes.

# Starting the Web API

There is a web API that is included with the `twitter-fire-scraper` package.

It exposes functions of the `twitter-fire-scraper` over HTTP. <!-- TODO Use HTTPS! -->

## From source

You can run the web API from the live source code with `pipenv run python twitter_fire_scraper/app.py`.

## Using PyPI

You can run the Web API after installing it with `pip` by typing

```
python -m twitter_fire_scraper.app
```

# Running tests

You can execute `pipenv run python fire-scraper/tests/<TESTNAME>.py` to run a test.

To run all tests, execute `pipenv run python fire-scraper/tests/test/__init__.py` and all tests will run.

Alternatively, if you have this package installed, run

```
python -m twitter_fire_scraper.tests.test
```

to run the package's test module.

# What was this adapted from?

A movie sentiment analysis project by [Raul](https://github.com/raaraa/), the repository [is here](https://github.com/raaraa/movie-twitter-sentiment) and a live site [is here](https://movie-tweet-sentiment.herokuapp.com/).

Commit `2fb844e8c081c1dc31cfb4760e3a80cefb6a0eee` was used.

# There's got to be a better way to run this than from the command line!

There is! Use an IDE (like PyCharm, which I use) that preferably integrates with Python to show you import errors, syntax errors, etc. Go google "Python IDE" and pick one you like.

# Adding the location of Venv to your IDE

<!-- TODO this section needs some polish! -->

 In order to run our tests through an IDE, we need to let our IDE know where venv was installed. I will explain this through Pycharm, but the method should be the same for any IDE.

If running `python` in windows powershell runs Python 3 (or you only have Python 3 installed), run `python -m pipenv --venv`

This will yield the location of the python 3 Virtual Environment (It should be something like `C:\Users\Your Name\...\.virtualenvs\...`). Copy this path and open Pycharm.

Go into `files -> settings` and expand the `Project: fire-scraper-twitter`. In the drop down, go into `Project Interpreter`. Go to the top and click the gear and select `add`, as we will be adding a new interpreter.

Select `Existing environment` and click the three dots to the right. Copy your path at the top, then OK everything.

There! Done! Now we can run our tests from inside our IDE.

# Generating/uploading distribution archives

If you want to distribute this source code as a Python Wheel, follow [this guide](https://packaging.python.org/tutorials/packaging-projects/).

There are a series of [Ruby](https://www.ruby-lang.org/en/) scripts (cross-platform!) that handle building, cleaning, uploading.

Make sure you have the `twine` package installed for Python.

## Building

```
ruby build.rb
```

## Cleaning

```
ruby clean.rb
```

## Uploading

You'll need to bump the version in `./VERSION` when uploading a new version.

### To the test site (test.pypi.org)

```
ruby upload.rb --test
```

### To the real site (pypi.org)

```
ruby upload.rb --deploy
```

## Testing download and install

There are a couple ways for you to test how a user would experience installing this package.

There are three Ruby scripts here, each doing what its name suggests.

`test-localwheel-install.rb` will install and test the latest WHL file generated by `build.rb`.

`test-testpypi-install.rb` will install and test the TEST PyPI's `twitter-fire-scraper` package.

`test-realpypi-install.rb` will install and test the offical PyPI's `twitter-fire-scraper` package.
