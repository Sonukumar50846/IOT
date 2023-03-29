import time


import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)
button=2
led1=3
led2=4
led3=27
led4=17

for i in range(4):
    gpio.setup(led1,gpio.HIGH)
    gpio.setup(led2,gpio.LOW)
    gpio.setup(led3,gpio.LOW)
    gpio.setup(led4,gpio.LOW)
    time.sleep(1)
    gpio.setup(led2,gpio.HIGH)
    gpio.setup(led1,gpio.LOW)
    gpio.setup(led3,gpio.LOW)
    gpio.setup(led4,gpio.LOW)
    time.sleep(1)
    gpio.setup(led3,gpio.HIGH)
    gpio.setup(led2,gpio.LOW)
    gpio.setup(led1,gpio.LOW)
    gpio.setup(led4,gpio.LOW)
    time.sleep(1)
    gpio.setup(led4,gpio.HIGH)
    gpio.setup(led2,gpio.LOW)
    gpio.setup(led3,gpio.LOW)
    gpio.setup(led1,gpio.LOW)
    time.sleep(1)