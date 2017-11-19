import RPi.GPIO as gpio
import time
import math
import smbus
from flask import Flask, request

app = Flask(__name__)

digital_output = 17
gpio.setmode(gpio.BCM)
bus = smbus.SMBus(1)

def adcSetup(Addr):
    global address
    address = Addr

def read(channel):
    if channel == 0:
        bus.write_byte(address,0x40)
    if channel == 1:
        bus.write_byte(address,0x41)
    if channel == 2:
        bus.write_byte(address,0x42)
    if channel == 3:
        bus.write_byte(address,0x43)
    bus.read_byte(address)
    return bus.read_byte(address)

def setup():
    adcSetup(0x48)
    gpio.setup(digital_output, gpio.IN)

def to_celcius(reading):
    vr = 5 * float(reading) / 255
    rt = 10000 * vr / (5 - vr)
    temperature = 1 / (((math.log(rt / 10000)) / 3950) + (1 / (273.15+25)))
    temperature = temperature - 273.15
    return temperature

def readTemp():
    reading = read(0)
    return str(round(to_celcius(reading), 2))

setup()

@app.route('/api/temperature', methods=['GET'])
def getTemperature():
    return readTemp()