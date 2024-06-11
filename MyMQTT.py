import sys
from Adafruit_IO import MQTTClient
from FSM import fsm

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
        if feed_id == "mixer1":
            fsm.run(client)