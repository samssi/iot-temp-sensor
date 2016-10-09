from sensor import sense

if __name__ == '__main__':
    #try:
    sense.setup()
    while True:
        sense.loop()
        #except KeyboardInterrupt:
        #       pass

