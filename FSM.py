import time
import Utilities.modbus485
import serial as serial
import config.m485_parameters as m485_params
from datetime import datetime

current_time = datetime.now().time()

class FSM:
    def __init__(self, cycle=1):
        self.state = 'idle'
        self.cycle = cycle
    
    def run(self, client):
        while self.state != 'end':
            if self.state == 'idle':
                self.idle_state()
            elif self.state == 'mixer1':
                self.mixer1_state(client)
            elif self.state == 'mixer2':
                self.mixer2_state(client)
            elif self.state == 'mixer3':
                self.mixer3_state(client)
            elif self.state == 'pumpin':
                self.pumpin_state(client)
            elif self.state == 'pumpout':
                self.pumpout_state(client)
    
    def idle_state(self):
        print("State: idle")
        self.state = 'mixer1'
    
    def mixer1_state(self, client):
        print("Cycle:", self.cycle)
        print("Time: ", datetime.now().time())
        print("State: mixer 1")
        m485.modbus485_send(m485_params.relay1_ON)
        time.sleep(0.5)
        if m485.modbus485_read_adc() == 255:
            print("Mixer 1 is on")
        else:
            print("Cannot turn on mixer 1")
        time.sleep(10)
        m485.modbus485_send(m485_params.relay1_OFF)
        client.publish("btl-iot.mixer1", 0)
        time.sleep(0.5)
        if m485.modbus485_read_adc() == 0:
            print("Mixer 1 is off")
        else:
            print("Cannot turn off mixer 1")
        self.state = 'mixer2'
    
    def mixer2_state(self, client):
        print("Time: ", datetime.now().time())
        print("State: mixer 2")
        m485.modbus485_send(m485_params.relay2_ON)
        client.publish("btl-iot.mixer2", 1)
        time.sleep(0.5)
        if m485.modbus485_read_adc() == 255:
            print("Mixer 2 is on")
        else:
            print("Cannot turn on mixer 2")
        time.sleep(10)
        m485.modbus485_send(m485_params.relay2_OFF)
        client.publish("btl-iot.mixer2", 0)
        time.sleep(0.5)
        if m485.modbus485_read_adc() == 0:
            print("Mixer 2 is off")
        else:
            print("Cannot turn off mixer 2")
        self.state = 'mixer3'

    def mixer3_state(self, client):
        print("Time: ", datetime.now().time())
        print("State: mixer 3")
        m485.modbus485_send(m485_params.relay3_ON)
        client.publish("btl-iot.mixer3", 1)
        time.sleep(0.5)
        if m485.modbus485_read_adc() == 255:
            print("Mixer 3 is on")
        else:
            print("Cannot turn on mixer 3")
        time.sleep(10)
        m485.modbus485_send(m485_params.relay3_OFF)
        client.publish("btl-iot.mixer3", 0)
        time.sleep(0.5)
        if m485.modbus485_read_adc() == 0:
            print("Mixer 3 is off")
        else:
            print("Cannot turn off mixer 3")
        self.state = 'pumpin'
    
    def pumpin_state(self, client):
        print("Time: ", datetime.now().time())
        print("State: pump in")
        time.sleep(15)
        client.publish("btl-iot.pumpin", 0)
        self.state = 'pumpout'
    
    def pumpout_state(self, client):
        print("Time: ", datetime.now().time())
        print("State: pump out")
        time.sleep(15)
        client.publish("btl-iot.pumpout", 0)
        if self.cycle > 1:
            self.cycle -= 1
            self.state = 'mixer1'
        else:
            self.state = 'end'

try:
    ser = serial.Serial(port='/dev/ttyUSB0', baudrate=9600)
except:
    print("Cannot open port")

m485 = Utilities.modbus485.Modbus485(ser)
fsm = FSM()

# if __name__ == "__main__":
#     fsm = FSM()
#     fsm.run()
#     print("FSM has reached the end state.")
