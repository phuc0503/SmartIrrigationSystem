import time

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
        time.sleep(10)
        self.state = 'mixer2'
    
    def mixer2_state(self):
        print("State: mixer 2")
        time.sleep(10)
        self.state = 'mixer3'

    def mixer3_state(self):
        print("State: mixer 3")
        time.sleep(10)
        self.state = 'pumpin'
    
    def pumpin_state(self):
        print("State: pump in")
        time.sleep(20)
        self.state = 'pumpout'
    
    def pumpout_state(self):
        print("State: pump out")
        time.sleep(20)
        self.state = 'end'

if __name__ == "__main__":
    fsm = FSM()
    fsm.run()
    print("FSM has reached the end state.")
