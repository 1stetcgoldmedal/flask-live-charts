flask-live-charts
=================

Live charting demo using flask and highcharts.

Simply run flask-live-charts.py and point your browser to http://127.0.0.1:5000

Tested on python 2.7.5 and 2.7.8 with Flask 0.10.1

Author : https://github.com/tdiethe/flask-live-charts

Edited
1. Publish random values ​​to mqtt broker (data-publisher.py)
2. Receive published values ​​from mqtt broker and save them to Mysql Database (data-collector.py)
3. In flask, periodically retrieve the latest data stored in mysql database and plot it as a graph (flask-live-chart.py)