/// <reference path="../library/ApiLibrary.ts" />
/*
 * GET home page.
 */
import express = require('express');
import { ApiLibrary } from '../library/ApiLibrary';

const router = express.Router();
const apiLibrary = new ApiLibrary()

router.get('/', async function (req: express.Request, res: express.Response) {

    var api_running = await apiLibrary.check_api()

    return res.render('index', {
        title: 'Twitter Fire Scraper Dashboard',
        api_status: (api_running ? "API OK!" : "API Unreachable."),
    });


});

router.all('/scrape', function (req: express.Request, res: express.Response) {

    var test_message;
    var statuses = undefined;

    if (req.method === 'POST') {
        // Retrieve tweets and display them

        const { terms, count } = req.body

        var count_number = Number(count)
        var terms_list = terms.replace('\r\n', ',')

        test_message = "You posted a form!"

        console.log(req.body)

        var tweets = apiLibrary.scrape_terms(terms_list, count_number)

        console.log(tweets["asd"])

    } else if (req.method === "GET") {
        // Do nothing, nothing to populate.

        test_message = "You are just sending a GET request."
    } else {
        return res.status(405).send(`The ${req.method} method for the "${req.originalUrl}" route is not supported.`);
    }

    return res.render('scrape', {
        title: 'Scrape new tweets',
        test_message: test_message,
        statuses: statuses
    })
});

export default router;