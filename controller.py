#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
import pigpio
from enum import Enum, unique, auto

pi = pigpio.pi()
pi.hardware_PWM(12, 8000, 10000)  # 10% duty cycle = 10000 (off)0 to (fully on)1000000

GPIO.setmode(GPIO.BOARD)        # Set up the pins on the board
GPIO.setwarnings(False)         # using the physical pin layout
GPIO.setup(29,GPIO.OUT)         # Physical pins 29 set as output
GPIO.setup(31,GPIO.OUT)         # Physical pins 31 set to output
GPIO.setup(37,GPIO.OUT)         # Physical pins 37 set to output
GPIO.setup(36,GPIO.OUT)         # Physical pins 36 set to output



class State(Enum):
    initial_state = auto()
    state_2 = auto()
    state_3 = auto()

class Controller:
    def __init__(self):
        self.current_state = State.initial_state
    
    def switch_states(self):
        if self.current_state == State.initial_state:
            GPIO.output(29,GPIO.HIGH)
            GPIO.output(31,GPIO.LOW)
            GPIO.output(37,GPIO.LOW)
            GPIO.output(36,GPIO.HIGH)
        elif self.current_state == State.state_2:
            GPIO.output(29,GPIO.LOW)
            GPIO.output(31,GPIO.HIGH)
            GPIO.output(37,GPIO.HIGH)
            GPIO.output(36,GPIO.LOW)
        elif self.current_state == State.state_3:
            GPIO.output(29,GPIO.HIGH)
            GPIO.output(31,GPIO.LOW)
            GPIO.output(37,GPIO.HIGH)
            GPIO.output(36,GPIO.LOW)
        else:
            GPIO.output(29,GPIO.HIGH)
            GPIO.output(31,GPIO.LOW)
            GPIO.output(37,GPIO.LOW)
            GPIO.output(36,GPIO.HIGH)
    
    def update_state(self):
        if self.current_state == State.initial_state:
            self.current_state = State.state_2
            self.switch_states()
        elif self.current_state == State.state_2:
            self.current_state = State.state_3
            self.switch_states()
        elif self.current_state == State.state_3:
            self.current_state = State.initial_state
            self.switch_states()
        else:
            self.current_state == State.initial_state


controller = Controller()       # Create the controller object from Controller class

while True:
    controller.update_state()
    time.sleep(1.5)
    controller.update_state()
    time.sleep(1.5)
    controller.update_state()
    time.sleep(1.5)

