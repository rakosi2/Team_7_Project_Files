#!/usr/bin/python3

# sudo pip3 install adafruit-circuitpython-ads1x15

import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

resistor = 0.00075

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1115(i2c)

# Create single-ended input on channel 0
#chan = AnalogIn(ads, ADS.P0)

# Create differential input between channel 0 and 1
chan1 = AnalogIn(ads, ADS.P0, ADS.P1)
#chan2 = AnalogIn(ads, ADS.P2, ADS.P3)

print("{:>5}\t{:>5}".format('raw', 'v', 'current'))

while True:
    print("{:>5}\t{:>5.3f}".format(chan1.value, chan1.voltage, chan1.voltage/resistor))
    time.sleep(0.5)