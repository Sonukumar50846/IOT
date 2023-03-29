import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.IN)
GPIO.setup(2,GPIO.OUT)
stop=0
while True:
    GPIO.output(17,False)
    time.sleep(0.5)
    
    GPIO.output(17,True)
    time.sleep(0.00001)
    GPIO.output(17,False)

    while GPIO.input(18)==0:
       start=time.time()
       
    while GPIO.input(18)==1:
       stop=time.time()
       
    time_interval=stop-start
    distance=time_interval*17000
    distance=round(distance,2)
    
    print(f"distance:{distance}")
    
    if distance<50:
        GPIO.output(2,GPIO.HIGH)
    else:
        GPIO.output(2,GPIO.LOW)        
   # print(f"distance:{distance}")
