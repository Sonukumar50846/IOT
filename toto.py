# importing gpio library
import RPi.GPIO as toto

# setting the RPi
toto.setmode(toto.BCM)

# initializing pin
button=2
led1=3
led2=4
led3=17
led4=27

# setting up all the inputs and outputs
toto.setup(led1,toto.OUT)
toto.setup(led2,toto.OUT)
toto.setup(led3,toto.OUT)
toto.setup(led4,toto.OUT)
toto.setup(button,toto.IN)

# loop
while True:
    
#     when btn pressed
    if toto.input(button)==1:
#       if toto.input(button)==1:
        toto.output(led1,toto.HIGH)
        toto.output(led2,toto.HIGH)
        toto.output(led3,toto.HIGH)
        toto.output(led4,toto.HIGH)
        
#         when btn not pressed
    else: 
        toto.output(led1,toto.LOW)
        toto.output(led2,toto.LOW)
        toto.output(led3,toto.LOW)
        toto.output(led4,toto.LOW)
    
