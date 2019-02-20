var current_data;

function sentiment_to_color(sentiment) {
    if (sentiment === 'positive') return 'panel-success';
    else if (sentiment === 'negative') return 'panel-danger';
    else return 'panel-primary';
}

function load_tweets(querystring) {
    $.ajax({
        url: 'tweets',
        data: {'query': querystring, 'retweets_only': 'false', 'with_sentiment': 'true'},
        dataType: 'json',
        type: 'GET',
        success: function (data) {
            buildChart(data);
            current_data = data['data'];
            var tweets = data['data'];
            var container = $('#tweets');
            var contents = '';
            contents += '<div>'

            for (i = 0; i < tweets.length; i++) {
                contents += '<div class="panel ' + sentiment_to_color(tweets[i].sentiment) + '"> <div class="panel-heading"> <h3 class="panel-title">' + tweets[i].user + '</h3> </div> <div class="panel-body"><blockquote>' + tweets[i].text + '</blockquote> </div> </div>'
                // contents += '<li class="list-group-item '+ sentiment_to_color(tweets[i].sentiment) +'">'+ tweets[i].user + ": " + tweets[i].text + '</li>';
            }

            contents += '</div>';
            container.html(contents);
            $('#query').val(querystring);
            $('#loading').html(data['count'] + " Tweets loaded about " + querystring + ".");
        }
    });
}

function load_movie(querystring) {
    $.ajax({
        url: 'movie',
        data: {'query': querystring},
        dataType: 'json',
        type: 'GET',
        success: function (data) {
            var movie = data['details'];
            var container = $('#movie');
            var contents = '';
            contents += '<div class="row">' +
                '<div class="col-md-4 col-md-offset-1">' +
                '<img src= " ' + movie[1] + '"/>' +
                '</div>' +
                '<div class="col-md-6 text-left">' +
                '<h3>' + movie[0] + '</h3>' + // Title
                '<p>' + 'Average Rating: ' + movie[4] + '</p>' + // Rating
                '<p>' + 'Release Date: ' + movie[3] + '</p>' + // Release date
                '<h4>' + 'Overview' + '</h4>' +
                '<p>' + movie[2] + '</p>' + // Overview
                '<iframe allowfullscreen="allowfullscreen" width="400" height="220" src= "' + movie[5] + '">' + '</iframe>' + // Overview
                '</div>' +
                '</div>'


            container.html(contents);
        }
    });
}

$(document).ready(function () {
    load_tweets('war for the planet of the apes');
});

$('#search').click(function () {
    $('#loading').html('Loading...');
    $('#tweets').html('');
    load_tweets($('#query').val());
    load_movie($('#query').val());
});

function buildChart(data) {
    Highcharts.chart('container', {
        chart: {
            plotBackgroundColor: null,
            plotBorderWidth: null,
            plotShadow: false,
            type: 'pie'
        },
        title: {
            text: 'last 100 tweets on ' + $('#query').val()
        },
        tooltip: {
            pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
        },
        plotOptions: {
            pie: {
                allowPointSelect: true,
                cursor: 'pointer',
                dataLabels: {
                    enabled: true,
                    format: '<b>{point.name}</b>: {point.percentage:.1f} %',
                    style: {
                        color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
                    }
                }
            }
        },
        series: getPercentage(data)
    });
};

function getNegativePercentage(data) {
    var current_data = data['data'];
    var counter = 0;
    for (var i = current_data.length - 1; i >= 0; i--) {
        if (current_data[i].sentiment == 'negative')
            counter++;
    }
    console.log('negative', counter)

    return counter / data.count;
}

function getPositivePercentage(data) {
    var current_data = data['data'];
    var counter = 0;
    for (var i = current_data.length - 1; i >= 0; i--) {
        if (current_data[i].sentiment == 'positive')
            counter++;
    }
    console.log('positive', counter)

    return counter / data.count;
}

function getNeutralPercentage(data) {
    var current_data = data['data'];
    var counter = 0;
    for (var i = current_data.length - 1; i >= 0; i--) {
        if (current_data[i].sentiment == 'neutral')
            counter++;
    }
    console.log('neutral', counter)
    return counter / data.count;
}

function getPercentage(data) {
    var neutral = getNeutralPercentage(data);
    var positive = getPositivePercentage(data);
    var negative = getNegativePercentage(data);

    return [{
        name: 'Tweets',
        //colorByPoint: true,
        data: [{
            name: 'Positive',
            y: positive,
            color: 'green'
        }, {
            name: 'Negative',
            y: negative,
            color: 'red',
            sliced: true,
            selected: true
        }, {
            name: 'Neutral',
            y: neutral,
            color: 'blue'
        }]
    }]
}
