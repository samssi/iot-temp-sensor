import smbus

bus = smbus.SMBus(1)

def setup(Addr):
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

def write(val):
    temp = val
    temp = int(temp)

    # print temp to see on terminal else comment out
    bus.write_byte_data(address, 0x40, temp)
