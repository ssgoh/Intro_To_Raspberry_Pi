#importing the Library
from gpiozero import LED,Button,Buzzer
from time import sleep
from signal import pause

#give name to components - variable
red_led = LED(14)
green_led=LED(18)
buzzer=Buzzer(25)
pc_button = Button(24)

#initialise state of components to off
red_led.off()
green_led.off()
buzzer.off()


#create a function for greenman
def greenman():
    sleep(10)
    red_led.off()
    green_led.on()
    sleep(15)
    green_led.blink(on_time=.5, off_time=.5, n=5)
    buzzer.blink(on_time=.5,off_time=.5,n=5)
    sleep(5)
    green_led.off()
    red_led.on()
    

#logic of program
red_led.on()
pc_button.when_pressed = greenman

pause()


