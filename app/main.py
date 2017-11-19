import PCF8581 as adc
import RPi.GPIO as gpio
import time
import math

digital_output = 17
gpio.setmode(gpio.BCM)

def setup():
    adc.setup(0x48)
    gpio.setup(digital_output, gpio.IN)

def to_celcius(reading):
    vr = 5 * float(reading) / 255
    rt = 10000 * vr / (5 - vr)
    temperature = 1 / (((math.log(rt / 10000)) / 3950) + (1 / (273.15+25)))
    temperature = temperature - 273.15
    print temperature

def read():
    reading = adc.read(0)
    to_celcius(reading)

if __name__ == '__main__':
    setup()
    read()