import paho.mqtt.client as mqtt
import pymysql.cursors
import json

#Setting Line Start
MQTT_BROKER_HOST = "test.mosquitto.org"
MQTT_BROKER_PORT = 1883
MQTT_TOPIC = "flask_live_chart/Temperature_Sensor"
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = ""
DB_NAME = "sensing"
#Setting Line End


connection = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME, cursorclass=pymysql.cursors.DictCursor)

def on_connect(MQTTclient, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    MQTTclient.subscribe(MQTT_TOPIC)

def on_message(MQTTclient, userdata, msg):
    print(f"{msg.topic} {str(msg.payload.decode('utf-8'))}")
    dict = None
    try:
        dict = json.loads(str(msg.payload.decode('utf-8')))
    except:
        return
    
    if(connection.open == False):
        connection.connect()

    #with connection:#connection
    with connection.cursor() as cursor:#cmd
        sql = "INSERT INTO `data` (`sensor_id`, `value`) VALUES (%s, %s)"
        cursor.execute(sql, (dict["sensor_id"], dict["value"]))
        connection.commit()

MQTTclient = mqtt.Client()
MQTTclient.on_connect = on_connect
MQTTclient.on_message = on_message
MQTTclient.connect(MQTT_BROKER_HOST, MQTT_BROKER_PORT, 60)
MQTTclient.loop_forever()