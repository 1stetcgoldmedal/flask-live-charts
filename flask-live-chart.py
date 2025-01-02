import json
from time import time
from random import random
from flask import Flask, render_template, make_response
import pymysql

#Setting Line Start
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = ""
DB_NAME = "sensing"
#Setting Line End

app = Flask(__name__)

connection = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME, cursorclass=pymysql.cursors.DictCursor)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/get_live_data')
def get_live_data():  
    if(connection.open == False):
        connection.connect()
    
    data = None
    with connection:
        with connection.cursor() as cursor:#cmd
            sql = "SELECT timestamp, value From data ORDER By idx DESC LIMIT 1"
            cursor.execute(sql)
            data = cursor.fetchall()

    data = [str(data[0]["timestamp"]), data[0]["value"]]
    print(data)
    response = make_response(data)
    response.content_type = 'application/json'
    return response

@app.route('/get_historical_data')
def get_historical_data():  
    if(connection.open == False):
        connection.connect()
    
    data = None
    with connection.cursor() as cursor:#cmd
        sql = "SELECT timestamp, value From data ORDER By idx ASC LIMIT 20"
        cursor.execute(sql)
        data = cursor.fetchall()

    transformed_data = [[str(item["timestamp"]), item["value"]] for item in data]
    return make_response(transformed_data)


if __name__ == '__main__':#웹서버 시작
    app.run(debug=True, host='127.0.0.1', port=5000)