#Example goes with Wiring Handout 1
#importing the Library
from gpiozero import LED
from time import sleep

#traffic light LEDs
tl_red = LED(13)
tl_amber = LED(19)
tl_green = LED(26)


#initialise state of components to off

#initialise traffic lights
tl_red.off()
tl_amber.off()
tl_green.off()


#assuming the traffic light starts with RED
tl.red.on()
sleep(10)
#after 10 seconds, RED goes off, GREEN comes on
tl.red.off()
tl_green.on()
sleep(10)
#After 10 secnds, GREEN goes off, AMBER starts to flash for 5 seconds
tl_green.off()
tl_amber.blink(on_time=.5, off_time=.5,n=5)
sleep(5)
#after 5 seconds, AMBER goes off, RED comes on
tl_amber.off()
tl_red.on()
    
   
    
