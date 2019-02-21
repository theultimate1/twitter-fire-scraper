# What is this?

TODO

# How do I run this?

## Setting up your secrets

You will need:

- A twitter developer account & API key
    - A consumer key
    - A consumer secret
    - An access token
    - An access secret

- A twitter handle you're authorized to make queries on behalf of

You are to put these into a file called `secrets.json` at the root of this directory.

An example file is provided for you to base your file off of, called `secrets.example.json`.

## Setting up a database

TODO mongodb

## Installing Python

This runs Python 2.7, so install Python 2.7

I used Pipenv, a Python dependency manager, to track and manage the packages
installed.

This is so everyone else can reproduce the Python environment I have on my
laptop/desktop.

### Setting up Pipenv

You can install Pipenv by running 
    
    python -m pip install pipenv

You can then install all packages in `./Pipenv` with

    pipenv install --two
    
Then, you can run the app with

    pipenv run python app.py
    
or run tests with

    pipenv run python tests.py

#### Troubleshooting Python2/3 issues

This section only really applies if you have both Python 2 and 3 installed.

Make sure that `python` refers to Python 2.7! If it doesn't, try going to
Python 2.7's installation directory and installing it via opening a shell there.

`where python` and `which python` can help you figure out the location of your
Python executables.

If you get odd errors and have both Python 2 and 3 (as I do), try appending
`--two` to the `pipenv` command to tell it to use Python 2.

If that doesn't work (or if `python` refers to Python 3), then using `python2 -m
pipenv install myCoolPackage` has a greater chance of working, assuming
`python2` refers to a Python 2.7 executable.

The nuclear option (uninstall Python 3 entirely) will definitely fix all these
problems.

# What was this adapted from?

A movie sentiment analysis project by [Raul](https://github.com/raaraa/), the
repository [is here](https://github.com/raaraa/movie-twitter-sentiment) and a
live site [is here](https://movie-tweet-sentiment.herokuapp.com/).

Commit `2fb844e8c081c1dc31cfb4760e3a80cefb6a0eee` was used.