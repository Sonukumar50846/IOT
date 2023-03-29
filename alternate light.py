import RPi.GPIO as toto
toto.setmode(toto.BCM)
button=2
led1=3

led2=4











led3=17  
led4=27

toto.setup(led1,toto.OUT)
toto.setup(led2,toto.OUT)
toto.setup(led3,toto.OUT)
toto.setup(led4,toto.OUT)
toto.setup(button,toto.IN)
while True:
    if toto.input(button)==1:
#   if toto.input(button)==1:
        toto.output(led1,toto.HIGH)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
        toto.output(led2,toto.HIGH)
        toto.output(led3,toto.HIGH)
        toto.output(led4,toto.HIGH)
    else: 
        #toto.output(led1,toto.LOW)
        toto.output(led2,toto.LOW)
        toto.output(led3,toto.LOW)
        #toto.output(led4,toto.LOW)
    
