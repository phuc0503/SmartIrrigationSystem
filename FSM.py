import time
import Utilities.modbus485
import serial as serial
import config.m485_parameters as m485_params

class FSM:
    def __init__(self):
        self.state = 'idle'
    
    def run(self):
        while self.state != 'end':
            if self.state == 'idle':
                self.idle_state()
            elif self.state == 'mixer1':
                self.mixer1_state()
            elif self.state == 'mixer2':
                self.mixer2_state()
            elif self.state == 'mixer3':
                self.mixer3_state()
            elif self.state == 'pumpin':
                self.pumpin_state()
            elif self.state == 'pumpout':
                self.pumpout_state()
    
    def idle_state(self):
        print("State: idle")
        self.state = 'mixer1'
    
    def mixer1_state(self):
        print("State: mixer 1")
        m485.modbus485_send(m485_params.relay1_ON)
        time.sleep(0.5)
        if m485.modbus485_read_adc() == 255:
            print("Mixer 1 is on")
        else:
            print("Cannot turn on mixer 1")
        time.sleep(10)
        m485.modbus485_send(m485_params.relay1_OFF)
        time.sleep(0.5)
        if m485.modbus485_read_adc() == 0:
            print("Mixer 1 is off")
        else:
            print("Cannot turn off mixer 1")
        self.state = 'mixer2'
    
    def mixer2_state(self):
        print("State: mixer 2")
        m485.modbus485_send(m485_params.relay2_ON)
        time.sleep(0.5)
        if m485.modbus485_read_adc() == 255:
            print("Mixer 2 is on")
        else:
            print("Cannot turn on mixer 2")
        time.sleep(10)
        m485.modbus485_send(m485_params.relay2_OFF)
        time.sleep(0.5)
        if m485.modbus485_read_adc() == 0:
            print("Mixer 2 is off")
        else:
            print("Cannot turn off mixer 2")
        self.state = 'mixer3'

    def mixer3_state(self):
        print("State: mixer 3")
        m485.modbus485_send(m485_params.relay3_ON)
        time.sleep(0.5)
        if m485.modbus485_read_adc() == 255:
            print("Mixer 3 is on")
        else:
            print("Cannot turn on mixer 3")
        time.sleep(10)
        m485.modbus485_send(m485_params.relay3_OFF)
        time.sleep(0.5)
        if m485.modbus485_read_adc() == 0:
            print("Mixer 3 is off")
        else:
            print("Cannot turn off mixer 3")
        self.state = 'pumpin'
    
    def pumpin_state(self):
        print("State: pump in")
        time.sleep(20)
        self.state = 'pumpout'
    
    def pumpout_state(self):
        print("State: pump out")
        time.sleep(20)
        self.state = 'end'

try:
    ser = serial.Serial(port='/dev/ttyUSB0', baudrate=9600)
except:
    print("Cannot open port")

m485 = Utilities.modbus485.Modbus485(ser)

if __name__ == "__main__":
    fsm = FSM()
    fsm.run()
    print("FSM has reached the end state.")
