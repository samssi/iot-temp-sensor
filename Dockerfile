FROM resin/rpi-raspbian:latest

RUN apt-get update && \
    apt-get -qy install curl ca-certificates

RUN apt-get install -y \
    build-essential \
    libi2c-dev \
    i2c-tools \
    python-dev \
    libffi-dev \
    python-rpi.gpio \
    python-smbus \
    python-pip

RUN pip install -U pip
RUN pip install virtualenv
RUN pip install flask

# Application setup
RUN mkdir -p /iot-tempsensor
WORKDIR /iot-tempsensor
ENV HOME /iot-tempsensor
COPY . /iot-tempsensor

ENV FLASK_APP=/iot-tempsensor/app/main.py

CMD ["flask", "run", "--host=0.0.0.0"]
