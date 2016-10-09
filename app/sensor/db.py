import psycopg2
import datetime

def insertTemperature(temperature):
    config = ""

    # print the connection string we will use to connect
    print "Connecting to database..."

    # get a connection, if a connect cannot be made an exception will be raised here
    connection = psycopg2.connect(config)

    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = connection.cursor()

    # execute our Query
    cursor.execute("INSERT INTO iot_temperature (sensor, measured_at, reading) VALUES (%s, %s, %s)", ("sensor1", datetime.datetime.now(), temperature))

    connection.commit()

    cursor.close()

    connection.close()
