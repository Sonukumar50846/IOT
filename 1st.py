import RPi.GPIO as gpio
import time 

gpio.setmode(gpio.BCM)  #for gpio no.
#or
#gpio.setmode(gpio.BOARD)  #for board no.

led=2
led1=3
led2=4

gpio.setup(led,gpio.OUT)
gpio.setup(led1,gpio.OUT)
gpio.setup(led2,gpio.OUT)

while True:
    gpio.output(led,gpio.HIGH)
    gpio.output(led1,gpio.LOW)
    gpio.output(led2,gpio.LOW)
    time.sleep(1)
    gpio.output(led2,gpio.HIGH)
    gpio.output(led,gpio.LOW)
    gpio.output(led1,gpio.LOW)
    
    time.sleep(1)
    gpio.output(led1,gpio.HIGH)
    gpio.output(led2,gpio.LOW)
    gpio.output(led,gpio.LOW)
    time.sleep(1)
    
    
    
