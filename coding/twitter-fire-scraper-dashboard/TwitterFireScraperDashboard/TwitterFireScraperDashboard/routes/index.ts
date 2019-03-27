/// <reference path="../library/ApiLibrary.ts" />
/*
 * GET home page.
 */
import express = require('express');
import { ApiLibrary } from '../library/ApiLibrary';
const router = express.Router();

router.get('/', async function(req: express.Request, res: express.Response) {


    var result = await ApiLibrary.check_api()

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