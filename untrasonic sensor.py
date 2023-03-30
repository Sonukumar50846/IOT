import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.IN)

stop=0

while True:
#     stopping sensor
    GPIO.output(17,False)
    time.sleep(0.5)
    
#     starting sensor for some microseconds
    GPIO.output(17,True)
    time.sleep(0.00001)
    
#     again stopping the sensor
    GPIO.output(17,False)

#     initializing start when input comes
    while GPIO.input(18)==0:
       start=time.time()
       
#     initializing stop when input stopes

    while GPIO.input(18)==1:
       stop=time.time()
       
#         time taken by wave to get back
    time_interval=stop-start
    
#     distance travelled by wave
    distance=time_interval*17000
    
#     rounding off the value
    distance=round(distance,2)
    
    
    print(f"distance:{distance} cm")
    
    
