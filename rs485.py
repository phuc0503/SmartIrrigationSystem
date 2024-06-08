import time
import serial.tools.list_ports

def getPort():
    ports = serial.tools.list_ports.comports()
    N = len(ports)
    commPort = "None"
    for i in range(0, N):
        port = ports[i]
        strPort = str(port)
        if "USB" in strPort:
            splitPort = strPort.split(" ")
            commPort = (splitPort[0])
    return commPort

portName = getPort()
print(portName)

if portName != "None":
    ser = serial.Serial(port=portName, baudrate=9600)
    print("Port opened successfully")
else:
    print("Cannot open port")

def serial_read_data(ser):
    bytesToRead = ser.inWaiting()
    if bytesToRead > 0:
        out = ser.read(bytesToRead)
        data_array = [b for b in out]
        print("Data array: ", data_array)
        print("Data array length: ", len(data_array))
        if len(data_array) >= 7:
            array_size = len(data_array)
            value = data_array[array_size - 4]*256 + data_array[array_size - 3]
            return value
        else:
            return -1
    return 0

relay_ON = [
    None,
    [1,6,0,0,0,255,201,138],
    [2,6,0,0,0,255,201,185],
    [3,6,0,0,0,255,200,104],
    [4,6,0,0,0,255,201,223],
    [5,6,0,0,0,255,200,14],
    [6,6,0,0,0,255,200,61],
    [7,6,0,0,0,255,201,236],
    [8,6,0,0,0,255,201,19]
]

relay_OFF = [
    None,
    [1,6,0,0,0,0,137,202],
    [2,6,0,0,0,0,137,249],
    [3,6,0,0,0,0,136,40],
    [4,6,0,0,0,0,137,159],
    [5,6,0,0,0,0,136,78],
    [6,6,0,0,0,0,136,152],
    [7,6,0,0,0,0,137,172],
    [8,6,0,0,0,0,137,83]
]

def setDevice(id, state):
    if state == True:
        print(relay_ON[id])
        ser.write(relay_ON[id])
    else:
        print(relay_OFF[id])
        ser.write(relay_OFF[id])
    print("Result: ", serial_read_data(ser))

soil_temperature = [10,3,0,6,0,1,101,112]

def readTemperature():
    serial_read_data(ser)
    ser.write(soil_temperature)
    time.sleep(1)
    return serial_read_data(ser)

soil_humidity = [10,3,0,6,0,1,101,112]

def readHumidity():
    serial_read_data(ser)
    ser.write(soil_humidity)
    time.sleep(1)
    return serial_read_data(ser)

while True:
    for i in range (1,8):
        setDevice(i, True)
        print("----------------")
        time.sleep(1)
        setDevice(i, False)
        print("----------------")
        time.sleep(1)