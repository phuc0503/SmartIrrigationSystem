from MyMQTT import *
import config.adafruit_cred as aio
from Utilities.modbus485 import *

mqtt_client = MyMQTTClient(aio.AIO_USERNAME, aio.AIO_KEY, aio.AIO_FEED_IDS)
mqtt_client.connect()

while True:
    # m485.modbus485_read_adc(mqtt_client.client)
    pass