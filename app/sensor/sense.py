import PCF8581 as adc
import db as db
import RPi.GPIO as gpio
import time
import math

digital_output = 17
gpio.setmode(gpio.BCM)

def setup():
    #       ADC.Setup(Address)  # Check it by sudo i2cdetect -y -1
    #       ADC.read(channal)       # Channal range from 0 to 3
    #       ADC.write(Value)        # Value range from 0 to 255
    adc.setup(0x48)
    gpio.setup(digital_output, gpio.IN)

def to_celcius(reading):
    vr = 5 * float(reading) / 255
    rt = 10000 * vr / (5 - vr)
    temperature = 1 / (((math.log(rt / 10000)) / 3950) + (1 / (273.15+25)))
    temperature = temperature - 273.15
    db.insertTemperature(temperature)
    print("temperature {0}".format(temperature))

def loop():
    reading = adc.read(0)
    to_celcius(reading)
    time.sleep(30)