import sys
from Adafruit_IO import MQTTClient
from FSM import fsm
from datetime import datetime
import time
from Utilities.modbus485 import *
import serial as serial
import config.m485_parameters as m485_params

class MyMQTTClient:
    def __init__(self, aio_username, aio_key, aio_feed_ids):
        self.client = MQTTClient(aio_username, aio_key)
        self.aio_feed_ids = aio_feed_ids

        self.client.on_connect = self.connected
        self.client.on_disconnect = self.disconnected
        self.client.on_message = self.message
        self.client.on_subscribe = self.subscribe
        
    def connect(self):
        self.client.connect()
        self.client.loop_background()

    def connected(self, client):
        print("Ket noi thanh cong")
        for topic in self.aio_feed_ids:
            self.client.subscribe(topic)

    def subscribe(self, client, userdata, mid, granted_qos):
        print("Subscribed thanh cong")

    def disconnected(self, client):
        print("Ngat ket noi")
        sys.exit (1)

    def message(self, client, feed_id, payload):
        # print("Nhan du lieu: " + payload, "feed id: " + feed_id)
        if feed_id == "iot-btl.mixer1" and payload == "1":
            # fsm.run(self.client)
            fsm.mixer1_state()
            self.client.publish("iot-btl.mixer1", 0)
            self.client.publish("iot-btl.mixer2", 1)
        if feed_id == "iot-btl.mixer2" and payload == "1":
            fsm.mixer2_state()
            self.client.publish("iot-btl.mixer2", 0)
            self.client.publish("iot-btl.mixer3", 1)
        if feed_id == "iot-btl.mixer3" and payload == "1":
            fsm.mixer3_state()
            self.client.publish("iot-btl.mixer3", 0)
        if feed_id  == "iot-btl.pumpin" and payload == "1":
            fsm.pumpin_state()
            self.client.publish("iot-btl.pumpin", 0)
        if feed_id == "iot-btl.pumpout" and payload == "1":
            fsm.pumpout_state()
            self.client.publish("iot-btl.pumpout", 0)