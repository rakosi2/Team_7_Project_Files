#!/usr/bin/python3
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(29,GPIO.OUT)

while True:
    GPIO.output(29,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(29,GPIO.LOW)
    time.sleep(1)







