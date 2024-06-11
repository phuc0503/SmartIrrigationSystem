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
        print("Nhan du lieu: " + payload, "feed id: " + feed_id)
        if feed_id == "iot-btl.mixer1" and payload == "1":
            # fsm.run(self.client)
            print("Time: ", datetime.now().time())
            print("State: mixer 1")
            m485.modbus485_send(m485_params.relay1_ON)
            time.sleep(0.5)
            if m485.modbus485_read_adc(self.client) == 255:
                print("Mixer 1 is on")
            else:
                print("Cannot turn on mixer 1")
            time.sleep(10)
            # self.client.publish("iot-btl.mixer1", 0)
            m485.modbus485_send(m485_params.relay1_OFF)
            time.sleep(0.5)
            if m485.modbus485_read_adc(self.client) == 0:
                print("Mixer 1 is off")
            else:
                print("Cannot turn off mixer 1")

            print("Time: ", datetime.now().time())
            print("State: mixer 2")
            # self.client.publish("iot-btl.mixer2", 1)
            m485.modbus485_send(m485_params.relay2_ON)
            time.sleep(0.5)
            if m485.modbus485_read_adc(self.client) == 255:
                print("Mixer 2 is on")
            else:
                print("Cannot turn on mixer 2")
            time.sleep(10)
            # self.client.publish("iot-btl.mixer2", 0)
            m485.modbus485_send(m485_params.relay2_OFF)
            time.sleep(0.5)
            if m485.modbus485_read_adc(self.client) == 0:
                print("Mixer 2 is off")
            else:
                print("Cannot turn off mixer 2")

            print("Time: ", datetime.now().time())
            print("State: mixer 3")
            # self.client.publish("iot-btl.mixer3", 1)
            m485.modbus485_send(m485_params.relay3_ON)
            time.sleep(0.5)
            if m485.modbus485_read_adc(self.client) == 255:
                print("Mixer 3 is on")
            else:
                print("Cannot turn on mixer 3")
            time.sleep(10)
            # self.client.publish("iot-btl.mixer3", 0)
            m485.modbus485_send(m485_params.relay3_OFF)
            time.sleep(0.5)
            if m485.modbus485_read_adc(self.client) == 0:
                print("Mixer 3 is off")
            else:
                print("Cannot turn off mixer 3")