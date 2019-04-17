# What is this?

A web frontend to allow you to use the `twitter-fire-scraper-webapi` package.

# Developers

## Dependencies

- Python 3

- [npm](https://www.npmjs.com/get-npm) version 6.7.0

- node v11.12.0
  
- `twitter-fire-scraper-webapi` web API running on port `3620`.

  You can go to `/coding/twitter-fire-scraper-webapi` to see how to
  bring up the web API.

## Running

`cd` into `./TwitterFireScraperDashboard/TwitterFireScraperDashboard/`.
All the below commands should take place in the same directory as `package.json`.

If you want to see a list of available commands, run `npm run`.

`npm run` and `npm run-script` do the same thing as far as I can tell.

1.  Run `npm install` to install packages that the project depends upon.

2.  Run `npm run-script build` to compile the TypeScript into JavaScript (debug error simultaneously). 

	Alternatively, you can run `npm run-script watch-tsc` to auto-build TypeScript into JavaScript when the TypeScript changes.

3.  Then, run `npm run-script start` to start the web application (run in a separate command prompt).

	Alternatively, you can run `npm run-script watch-node` to auto-reload the Node.js web app.

4.	To visit the site, go to `localhost:3000`.

This web application will attempt to detect if the TwitterFireScraper web API is running and will notify you if it is successful.

## Developing

Use Visual Studio with Node.js installed. TODO make more verbose

TODO elaborate <see `package.json` for `watch-*` build steps>
