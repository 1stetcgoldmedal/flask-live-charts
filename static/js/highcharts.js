var chart;

function requestData() {
    $.ajax({
        url: '/get_live_data',
        success: function(point) {
            if(chart.series[0].data.length == 0)
            {
                chart.series[0].addPoint(point, true, false);
            }

            console.log(point[0])
            if(chart.series[0].data[chart.series[0].data.length - 1].name != point[0])
            {
                shift = chart.series[0].data.length > 20;
                chart.series[0].addPoint(point, true, shift);
            }
            setTimeout(requestData, 5000);
        },
        cache: false
    });
}


function requestHistoricalData() {
    $.ajax({
        // url: '/get_live_data',
        url: '/get_historical_data',
        success: function(point) {
            chart.series[0].setData(point);
            setTimeout(requestData, 1000);
        },
        cache: false
    });
}

$(document).ready(function() {
    chart = new Highcharts.Chart({
        chart: {
            renderTo: 'data-container',
            defaultSeriesType: 'spline',
            events: {
                load: requestHistoricalData
            }
        },
        title: {
            text: 'Live random data'
        },
        xAxis: {
            type: 'datetime',
            tickPixelInterval: 150,
            maxZoom: 20
        },
        yAxis: {
            minPadding: 0.2,
            maxPadding: 0.2,
            title: {
                text: 'Value',
                margin: 80
            }
        },
        series: [{
            name: 'Random data',
            data: []
        }]
    });
});