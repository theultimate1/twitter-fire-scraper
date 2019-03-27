import request = require('request');
import url = require('url')

export class ApiLibrary {
    /**
 * @param host Host of web API.
 * @param port Port of web API.
 * @param path Path to web API info.
 * 
 * Checks if the twitter-fire-scraper-webapi is functioning correctly.
 */
    static check_api(host: string = "http://127.0.0.1", port: string = "3620", path: string = "info") {
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

}