#Library
from gpiozero import LED, Buzzer, Button
from time import sleep
from signal import pause

#setup
blue=LED(21)
red=LED(14)
buzz=Buzzer(20)
button=Button(16)

#initialize
blue.off()
red.off()

#Algorithm
buzz.on()
while True:
    blue.blink(on_time=.1,off_time=.1,n=1)
    sleep(.1)
    blue.off()
    buzz.blink(on_time=.1,off_time=.1,n=1)
    red.blink(on_time=.1,off_time=.1,n=1)
    sleep(.1)
    red.off()
    
