By Henry Post

This is a list of tasks that should be worked on by the coding team after Spring
Break.

1.  Expose our Scraper's interface via a web API 

    1.  Create a **_separate_** Flask application that **_uses_** the
    `twitter-fire-scraper` package.
    
    It could be called `twitter-fire-scraper-webapi`, for example.
    
    This is separate to avoid having our `twitter-fire-scraper` package be one
    gigantic app.
    
    2.  Route API endpoints to functions (due 03/31)

        e.g.:
        
        `Scraper.scrape(terms={"fire","chicagofire"})` goes to
        
        `localhost:5555/scraper/scrape?terms="pizza,chicagofire"`
        
        This is to allow the Node.js application to use the
        `twitter-fire-scraper` even though they are written in different
        languages.
        
        These API functions should both save the tweets to a MongoDB Database and also
        return the scraped tweets as JSON.

2.  Make a Node.js web application to consume the Flask application's service.
    
    It should be able to display: 
    
    1.  A dashboard of new tweets (due 04/07)

    2.  A map of tweets (geolocated ones) (due 04/14)

    3.  A way to search for saved tweets (think MongoDB Compass) (due 04/14)

    4.  A way to delete tweets (due 04/21)

    5.  A way to scrape new tweets! (due 04/21)
    
3.  Make extended scraping unit-tests that verify the scraper's ability to
search large amounts of tweets. (due 03/31)

4.  Add a `scrape_and_save(...)` method (due 04/21) to the `Scraper` class that allows you to
    both scrape terms/accounts and then save them to a MongoDB database.
    
    This functionality should then be added to the web API. (due 04/28)
    
    This is to make scraping and saving to the MongoDB database via the web API simple.

Some notes:

Ideally, any new functionality should have some sort of test to make sure it works.
