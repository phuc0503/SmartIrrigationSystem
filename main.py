from MyMQTT import *
import config.adafruit_cred as aio

mqtt_client = MyMQTTClient(aio.AIO_USERNAME, aio.AIO_KEY, aio.AIO_FEED_IDS)
mqtt_client.connect()

while True:
    pass