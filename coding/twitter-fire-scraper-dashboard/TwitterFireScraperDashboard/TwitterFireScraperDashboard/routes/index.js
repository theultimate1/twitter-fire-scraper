"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : new P(function (resolve) { resolve(result.value); }).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
Object.defineProperty(exports, "__esModule", { value: true });
/*
 * GET home page.
 */
const express = require("express");
const request = require("request");
const url = require("url");
const router = express.Router();
/**
 * @param host Host of web API.
 * @param port Port of web API.
 * @param path Path to web API info.
 *
 * Checks if the twitter-fire-scraper-webapi is functioning correctly.
 */
function check_api(host = "http://127.0.0.1", port = "3620", path = "info") {
    var uri = new url.URL(host);
    uri.port = port.toString();
    uri.pathname = path;
    return new Promise((resolve, reject) => {
        request(uri.href, (err, res, body) => {
            if (err) {
                resolve(false);
            }
            if (body === "twitter-fire-scraper-webapi") {
                console.log("It's the real API.");
                resolve(true);
            }
            else {
                resolve(false);
            }
        });
    });
}
router.get('/', function (req, res) {
    return __awaiter(this, void 0, void 0, function* () {
        var result = yield check_api();
        if (result === null) {
            throw "Async code failed to run! Why???";
        }
        else {
            console.log("Async code ran! :)");
            console.log(result);
        }
        console.log("Rendering...");
        return res.render('index', {
            title: 'Express',
            api_status: (result ? "API OK!" : "API Unreachable."),
        });
    });
});
exports.default = router;
//# sourceMappingURL=index.js.map