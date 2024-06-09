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
            elif self.state == 'pumpout':
                self.pumpout_state()
    
    def idle_state(self):
        print("State: idle")
        self.state = 'mixer1'
    
    def mixer1_state(self):
        print("State: mixer1")
        time.sleep(10)
        self.state = 'mixer2'
    
    def mixer2_state(self):
        print("State: mixer2")
        time.sleep(10)
        self.state = 'pumpout'
    
    def pumpout_state(self):
        print("State: pumpout")
        time.sleep(20)
        self.state = 'end'

if __name__ == "__main__":
    fsm = FSM()
    fsm.run()
    print("FSM has reached the end state.")
