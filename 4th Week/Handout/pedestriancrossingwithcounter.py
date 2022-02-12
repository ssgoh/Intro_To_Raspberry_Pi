#importing the Library
from gpiozero import LED,Button,Buzzer
from time import sleep
from signal import pause

#introducint TM1637 to program
import tm1637
display = tm1637.TM1637(20, 16) #20=CLK  16=DIO

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
    sleep(10)
    #introducing the counter here
    for count in range(9,-1,-1):
        
        green_led.blink(on_time=.5, off_time=.5, n=1)
        buzzer.blink(on_time=.5,off_time=.5,n=1)
        S1=' '
        S2=' '
        S3=' '
        S4=str(count)
        display.set_values([S1, S2, S3, S4])
        sleep(1)
    
    green_led.off()
    display.clear()
    red_led.on()
    

#logic of program
red_led.on()
pc_button.when_pressed = greenman

pause()


