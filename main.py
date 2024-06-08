from MyMQTT import *

AIO_FEED_IDS = ["iot-btl.area1", 
                "iot-btl.area2", 
                "iot-btl.area3",
                "iot-btl.mixer1",
                "iot-btl.mixer2",
                "iot-btl.mixer3",
                "iot-btl.pumpin",
                "iot-btl.pumpout"
                ]

AIO_USERNAME = "hungle2002"
AIO_KEY = ""

mqtt_client = MyMQTTClient(AIO_USERNAME, AIO_KEY, AIO_FEED_IDS)
mqtt_client.connect()

while True:
    pass