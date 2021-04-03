#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
import pigpio
from enum import Enum, unique, auto

pi = pigpio.pi()
pi.hardware_PWM(12, 8000, 10000)  # 10% duty cycle = 10000 (off)0 to (fully on)1000000

GPIO.setmode(GPIO.BOARD)        # Set up the pins on the board using the physical pin layout
GPIO.setwarnings(False)
PIN1 = 29                       # These should remain constant
PIN2 = 31                       # These should remain constant
PIN3 = 36                       # These should remain constant
PIN4 = 37                       # These should remain constant
GPIO.setup(PIN1,GPIO.OUT)         # Physical pins 29 set as output
GPIO.setup(PIN2,GPIO.OUT)         # Physical pins 31 set to output
GPIO.setup(PIN3,GPIO.OUT)         # Physical pins 36 set to output
GPIO.setup(PIN4,GPIO.OUT)         # Physical pins 37 set to output


@unique
class State(Enum):
    state_1 = auto()
    state_2 = auto()
    state_3 = auto()
    state_4 = auto()
    state_5 = auto()
    state_6 = auto()
    state_7 = auto()

class Controller:
    def __init__(self):
        self.current_state = State.state_1
        self.switch_states()
    
    def switch_states(self):
        if self.current_state == State.state_1:
            GPIO.output(PIN1,GPIO.LOW)      # OFF
            GPIO.output(PIN2,GPIO.HIGH)     # ON
            GPIO.output(PIN3,GPIO.HIGH)     # ON
            GPIO.output(PIN4,GPIO.LOW)      # OFF
        elif self.current_state == State.state_2:
            GPIO.output(PIN1,GPIO.HIGH)     # ON
            GPIO.output(PIN2,GPIO.LOW)      # OFF
            GPIO.output(PIN3,GPIO.LOW)      # OFF
            GPIO.output(PIN4,GPIO.HIGH)     # ON
        elif self.current_state == State.state_3:
            GPIO.output(PIN1,GPIO.HIGH)     # ON
            GPIO.output(PIN2,GPIO.HIGH)     # ON
            GPIO.output(PIN3,GPIO.LOW)      # OFF
            GPIO.output(PIN4,GPIO.LOW)      # OFF
        elif self.current_state == State.state_4:
            GPIO.output(PIN1,GPIO.HIGH)     # ON
            GPIO.output(PIN2,GPIO.HIGH)     # ON
            GPIO.output(PIN3,GPIO.HIGH)     # ON
            GPIO.output(PIN4,GPIO.LOW)      # OFF
        elif self.current_state == State.state_5:
            GPIO.output(PIN1,GPIO.HIGH)     # ON
            GPIO.output(PIN2,GPIO.HIGH)     # ON
            GPIO.output(PIN3,GPIO.HIGH)     # ON
        elif self.current_state == State.state_6:
            GPIO.output(PIN1,GPIO.HIGH)     # ON
            GPIO.output(PIN2,GPIO.HIGH)     # ON
            GPIO.output(PIN3,GPIO.HIGH)     # ON
            GPIO.output(PIN4,GPIO.HIGH)     # ON
        elif self.current_state == State.state_7:
            GPIO.output(PIN1,GPIO.HIGH)     # ON
            GPIO.output(PIN2,GPIO.LOW)      # OFF
            GPIO.output(PIN3,GPIO.HIGH)     # ON
            GPIO.output(PIN4,GPIO.HIGH)     # ON
        else:
            GPIO.output(PIN1,GPIO.LOW)      # OFF
            GPIO.output(PIN2,GPIO.HIGH)     # ON
            GPIO.output(PIN3,GPIO.HIGH)     # ON
            GPIO.output(PIN4,GPIO.LOW)      # OFF
    
    def update_state(self, next_state):
        self.current_state = next_state
        self.switch_states()
        
    
    def print_status(self):
        print(self.current_state.name)
        print("Pin 1: On" if GPIO.input(PIN1) else "Pin 1: Off")
        print("Pin 2: On" if GPIO.input(PIN2) else "Pin 2: Off")
        print("Pin 3: On" if GPIO.input(PIN3) else "Pin 3: Off")
        print("Pin 4: On" if GPIO.input(PIN4) else "Pin 4: Off")




