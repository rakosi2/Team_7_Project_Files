#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
import pigpio
from enum import Enum, unique, auto

pi = pigpio.pi()
pi.hardware_PWM(12, 8000, 10000)  # 10% duty cycle = 10000 (off)0 to (fully on)1000000

GPIO.setmode(GPIO.BOARD)        # Set up the pins on the board
GPIO.setwarnings(False)         # using the physical pin layout
GPIO.setup(29,GPIO.OUT)         # Physical pins 29 set to out
GPIO.setup(31,GPIO.OUT)         # Physical pins 31 set to out
GPIO.setup(37,GPIO.OUT)         # Physical pins 37 set to out
GPIO.setup(36,GPIO.OUT)         # Physical pins 36 set to out


@unique
class State(Enum):
    initial_state = auto()
    state_2 = auto()
    state_3 = auto()

class Controller:
    def __init__(self):
        self.current_state = State.initial_state
    
    def get_next_state:
        pass
    

controller = Controller()




while True:
    GPIO.output(29,GPIO.HIGH)
    time.sleep(0.10)
    GPIO.output(29,GPIO.LOW)
    GPIO.output(31,GPIO.HIGH)
    time.sleep(0.10)
    GPIO.output(31,GPIO.LOW)
    GPIO.output(37,GPIO.HIGH)
    time.sleep(0.10)
    GPIO.output(37,GPIO.LOW)
    GPIO.output(36,GPIO.HIGH)
    time.sleep(0.10)
    GPIO.output(36,GPIO.LOW)



