import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
time.sleep(2)

GPIO.output(16, GPIO.HIGH)
print("Pin 16 HIGH")
time.sleep(2)
GPIO.output(16, GPIO.LOW)
print("Pin 16 LOW")
time.sleep(2)

GPIO.output(20, GPIO.HIGH)
print("Pin 20 HIGH")
time.sleep(2)
GPIO.output(20, GPIO.LOW)
print("Pin 20 LOW")
time.sleep(2)

GPIO.output(21, GPIO.HIGH)
print("Pin 21 HIGH")
time.sleep(2)
GPIO.output(21, GPIO.LOW)
print("Pin 21 LOW")
time.sleep(2)

GPIO.output(26, GPIO.HIGH)
print("Pin 26 HIGH")
time.sleep(2)
GPIO.output(26, GPIO.LOW)
print("Pin 26 LOW")
time.sleep(2)

GPIO.cleanup()