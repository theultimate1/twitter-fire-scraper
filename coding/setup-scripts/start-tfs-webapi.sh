pushd twitter-fire-scraper-webapi

pipenv run pip install pip==18.0
pipenv install

pipenv run python src/twitter_fire_scraper_webapi/app.py 2> /tmp/flask.error.log > /tmp/flask.log & # TODO This is still a race condition. Just one unlikely to fail...
FLASK_PID=$!
sleep 30

echo PID of flask web server is ${FLASK_PID}
curl -v 127.0.0.1:3620

popd