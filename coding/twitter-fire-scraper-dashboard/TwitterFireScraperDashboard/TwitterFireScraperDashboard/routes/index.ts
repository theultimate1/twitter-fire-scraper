/// <reference path="../library/ApiLibrary.ts" />
/*
 * GET home page.
 */
import express = require('express');
import { ApiLibrary } from '../library/ApiLibrary';

const router = express.Router();
const apiLibrary = new ApiLibrary()

router.get('/', async function(req: express.Request, res: express.Response) {

    var api_running = await apiLibrary.check_api()
    
    return res.render('index', {
        title: 'Twitter Fire Scraper Dashboard',
        api_status: (api_running ? "API OK!" : "API Unreachable."),
    });


});

router.all('/scrape', function (req: express.Request, res: express.Response) {

    var data;

    if (req.method === 'POST') {
        // Retrieve tweets and display them

        const { terms, count } = req.body

        data="You posted a form!"

        console.log(req.body)
        
    } else if (req.method === "GET") {
        // Do nothing, nothing to populate.

        data = "You are just sending a GET request."
    } else {
        return res.status(405).send(`The ${req.method} method for the "${req.originalUrl}" route is not supported.`);
    }

    return res.render('scrape', {
        title: 'Scrape new tweets',
        data: data,
    })
});

export default router;