#!/usr/bin/env bash

pushd code/twitter-fire-scraper/

    pipenv run pip install pip==18.0
    pipenv install --three

    pipenv run python -m twitter_fire_scraper.app 2> /tmp/flask.error.log > /tmp/flask.log & # TODO This is still a race condition. Just one unlikely to fail...
    FLASK_PID=$!
    sleep 30

    echo PID of flask web server is ${FLASK_PID}
    curl -v 127.0.0.1:3620

popd