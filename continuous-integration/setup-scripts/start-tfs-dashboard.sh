pushd twitter-fire-scraper-dashboard/TwitterFireScraperDashboard/TwitterFireScraperDashboard

npm install
npm run build

npm run serve 2> /tmp/node.error.log > /tmp/node.log & # TODO This is still a race condition. Just one unlikely to fail...
NPM_PID=$!
sleep 30

echo PID of node web server is ${NPM_PID}
curl -v localhost:3000

popd