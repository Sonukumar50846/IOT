# imported time
import time

# imported GPIO 
import RPi.GPIO as gpio

# setting mode of RPi
gpio.setmode(gpio.BCM)

# initializing
button=2
led1=3
led2=4
led3=27
led4=17

# loop
for i in range(4):
#     switching on led1 and off others
    gpio.setup(led1,gpio.HIGH)
    gpio.setup(led2,gpio.LOW)
    gpio.setup(led3,gpio.LOW)
    gpio.setup(led4,gpio.LOW)
    time.sleep(1)
#     switching on led1 and off others    
    gpio.setup(led2,gpio.HIGH)
    gpio.setup(led1,gpio.LOW)
    gpio.setup(led3,gpio.LOW)
    gpio.setup(led4,gpio.LOW)
    time.sleep(1)
#     switching on led1 and off others    
    gpio.setup(led3,gpio.HIGH)
    gpio.setup(led2,gpio.LOW)
    gpio.setup(led1,gpio.LOW)
    gpio.setup(led4,gpio.LOW)
    time.sleep(1)
#     switching on led1 and off others    
    gpio.setup(led4,gpio.HIGH)
    gpio.setup(led2,gpio.LOW)
    gpio.setup(led3,gpio.LOW)
    gpio.setup(led1,gpio.LOW)
    time.sleep(1)
