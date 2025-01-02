import paho.mqtt.client as mqtt
import pymysql.cursors
import json
import time
import random

#Setting Line Start
MQTT_BROKER_HOST = "test.mosquitto.org"
MQTT_BROKER_PORT = 1883
MQTT_TOPIC = "flask_live_chart/Temperature_Sensor"
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = ""
DB_NAME = "sensing"

SENSOR_ID = 1
#Setting Line End

def on_connect(MQTTclient, userdata, flags, rc):
    print("Connected with result code " + str(rc))

def on_publish(MQTTClient, userdata, mid):
    print("Published")

def generate_random_number():
    return random.randint(1, 100)

MQTTclient = mqtt.Client()
MQTTclient.on_connect = on_connect
MQTTclient.on_publish = on_publish
MQTTclient.connect(MQTT_BROKER_HOST, MQTT_BROKER_PORT, 60)
MQTTclient.loop_start()
json_data = {
    "sensor_id": SENSOR_ID,
    "value" : generate_random_number()
}
while(True):
    MQTTclient.publish(topic=MQTT_TOPIC, payload=json.dumps(json_data))
    json_data["value"] = generate_random_number()
    time.sleep(5)