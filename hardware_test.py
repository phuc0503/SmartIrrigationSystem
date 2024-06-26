import Utilities.modbus485
import serial as serial
import time

try:
    ser = serial.Serial(port='/dev/ttyUSB0', baudrate=9600)
except:
    print("Cannot open port")

m485 = Utilities.modbus485.Modbus485(ser)

relay1_ON  = [1,6,0,0,0,255,201,138]
relay1_OFF = [1,6,0,0,0,0,137,202]

relay2_ON  = [2,6,0,0,0,255,201,185]
relay2_OFF = [2,6,0,0,0,0,137,249]

relay3_ON  = [3,6,0,0,0,255,200,104]
relay3_OFF = [3,6,0,0,0,0,136,40]

relay4_ON  = [4,6,0,0,0,255,201,223]
relay4_OFF = [4,6,0,0,0,0,137,159]

relay5_ON  = [5,6,0,0,0,255,200,14]
relay5_OFF = [5,6,0,0,0,0,136,78]

relay6_ON  = [6,6,0,0,0,255,200,61]
relay6_OFF = [6,6,0,0,0,0,136,125]

relay7_ON  = [7,6,0,0,0,255,201,236]
relay7_OFF = [7,6,0,0,0,0,137,172]

relay8_ON  = [8,6,0,0,0,255,201,19]
relay8_OFF = [8,6,0,0,0,0,137,83]

m485.modbus485_send(relay1_ON)
time.sleep(1)
# m485.modbus485_send(relay2_ON)
# time.sleep(1)
# m485.modbus485_send(relay3_ON)
# time.sleep(1)
# m485.modbus485_send(relay4_ON)
# time.sleep(1)
# m485.modbus485_send(relay5_ON)
# time.sleep(1)
# m485.modbus485_send(relay6_ON)
# time.sleep(1)
# m485.modbus485_send(relay7_ON)
# time.sleep(1)
# m485.modbus485_send(relay8_ON)
# time.sleep(1)

m485.modbus485_send(relay1_OFF)
time.sleep(1)
# m485.modbus485_send(relay2_OFF)
# time.sleep(1)
# m485.modbus485_send(relay3_OFF)
# time.sleep(1)
# m485.modbus485_send(relay4_OFF)
# time.sleep(1)
# m485.modbus485_send(relay5_OFF)
# time.sleep(1)
# m485.modbus485_send(relay6_OFF)
# time.sleep(1)
# m485.modbus485_send(relay7_OFF)
# time.sleep(1)
# m485.modbus485_send(relay8_OFF)
# time.sleep(1)

print("Result: ", m485.modbus485_read_adc())