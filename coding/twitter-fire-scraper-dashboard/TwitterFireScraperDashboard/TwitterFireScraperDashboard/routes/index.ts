/*
 * GET home page.
 */
import express = require('express');
import request = require('request');
import url = require('url')
const router = express.Router();

/**
 * @param host Host of web API.
 * @param port Port of web API.
 * @param path Path to web API info.
 * 
 * Checks if the twitter-fire-scraper-webapi is functioning correctly.
 */
function check_api(host = "http://127.0.0.1", port = "3620", path = "info") {
    var uri = new url.URL(host)
    uri.port = port.toString()
    uri.pathname = path

    return new Promise((resolve, reject) => {
        request(uri.href, (err, res, body) => {
            if (err) {
                resolve(false)
            }

            if (body === "twitter-fire-scraper-webapi") {
                console.log("It's the real API.")
                resolve(true)
            }
            else {
                resolve(false)
            }
        })
    })
}

router.get('/', async function(req: express.Request, res: express.Response) {


    var result = await check_api()

    if (result === null) {
        throw "Async code failed to run! Why???"
    } else {
        console.log("Async code ran! :)")
        console.log(result)
    }

    console.log("Rendering...")

    return res.render('index', {
        title: 'Express',
        api_status: (result ? "API OK!" : "API Unreachable."),
    });


});

export default router;