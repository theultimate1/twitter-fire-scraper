# What is this?

A web frontend to allow you to use the `twitter-fire-scraper` package via the
web.

# Developers

## Running

Install `npm`, [Node Package Manager](https://www.npmjs.com/get-npm).

Then, `cd` into `./TwitterFireScraperDashboard/TwitterFireScraperDashboard/`.
All the below commands should take place in the same directory as `package.json`.

1.  Run `npm install` to install packages that the project depends upon.

2.  Run `npm build` to compile the TypeScript into JavaScript.

	Alternatively, you can run `npm watch-tsc` to auto-build TypeScript into JavaScript when the TypeScript changes.

3.  Then, run `npm start` to start the web application.

	Alternatively, you can run `npm watch-node` to auto-reload the Node.js web app.

4.	To visit the site, go to `localhost:3000`.

This web application will attempt to detect if the TwitterFireScraper web API is running and will notify you if it is successful.

## Developing

Use Visual Studio with Node.js installed. TODO make more verbose

TODO elaborate <see `package.json` for `watch-*` build steps>