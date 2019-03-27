/// <reference path="../library/ApiLibrary.ts" />
/*
 * GET home page.
 */
import express = require('express');
import { ApiLibrary } from '../library/ApiLibrary';
const router = express.Router();

router.get('/', async function(req: express.Request, res: express.Response) {

    var api_running = await ApiLibrary.check_api()
    
    return res.render('index', {
        title: 'Express',
        api_status: (api_running ? "API OK!" : "API Unreachable."),
    });


});

export default router;