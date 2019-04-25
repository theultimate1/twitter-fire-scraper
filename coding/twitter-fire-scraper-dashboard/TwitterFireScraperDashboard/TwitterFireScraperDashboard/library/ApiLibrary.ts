import request = require('request');
import url = require('whatwg-url');
import querystring = require('querystring')
import { URL } from 'url';

export class ApiLibrary {
    /**
     * @param host Host of web API.
     * @param port Port of web API.
     * @param path Path to web API info.
     * 
     * Checks if the twitter-fire-scraper-webapi is functioning correctly.
     */
    host: string;
    port: string;

    constructor(
        host: string = "http://127.0.0.1",
        port: string = "3620") {

        this.host = host;
        this.port = port;
    }

    construct_uri() {
        var uri = new url.URL(this.host)
        uri.port = this.port.toString()
        return uri
    }

    check_api(path: string = "info") {
        var uri = this.construct_uri()
        uri.pathname = path

        return new Promise((resolve, reject) => {
            request(uri.href, (err, res, body) => {
                if (err) {
                    resolve(false)
                }

                if (body === "twitter-fire-scraper-webapi") {
                    console.log("API OK!")
                    resolve(true)
                }
                else {
                    resolve(false)
                }
            })
        })
    }

    scrape_terms(terms: Array<String>, count: Number): Promise<JSON> {
        var uri: URL = this.construct_uri()

        uri.pathname = "scrape_terms"

        var args: string = querystring.stringify({ terms: terms, count: count });

        var query_string = uri.href + "?" + args // TODO this is insecure.

        console.log("our query string:")

        console.log(query_string)

        return new Promise((resolve, reject) => {

            request(query_string, (err, res, body) => {

                if (err) {
                    throw err;
                }

                console.log("Got response!")

                console.log(body)

                resolve(JSON.parse(body))
            })


        })
    }

    scrape_accounts(accounts: string, count: Number): Promise<JSON> {
        var uri: URL = this.construct_uri()
        uri.pathname = "scrape_accounts"

        var args: string = querystring.stringify({ accounts: accounts, count: count });
        console.log(args)
        var query_string = uri.href + "?" + args // TODO this is insecure.

        console.log("our query string:")

        console.log(query_string)

        return new Promise((resolve, reject) => {

            request(query_string, (err, res, body) => {

                if (err) {
                    throw err;
                }

                console.log("Got response!")

                console.log(body)

                resolve(JSON.parse(body))
            })


        })
    }
}