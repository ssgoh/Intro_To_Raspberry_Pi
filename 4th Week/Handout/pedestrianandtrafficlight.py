#importing the Library
from gpiozero import LED,Button,Buzzer
from time import sleep
from signal import pause

#introducing TM1637 to program
import tm1637


#give name to components - variable
display = tm1637.TM1637(20, 16) #20=CLK  16=DIO
red_led = LED(14)
green_led=LED(18)
buzzer=Buzzer(25)
pc_button = Button(24)

#add anti spam LED here
anti_spam_led=LED(7)

#traffic light LEDs
tl_red = LED(13)
tl_amber = LED(19)
tl_green = LED(26)


#initialise state of components to off
#initialise pedestrian crossing lights
red_led.off()
green_led.off()
buzzer.off()

#initialise traffic lights
tl_red.off()
tl_amber.off()
tl_green.off()

#must initialise the anti spam LED as well
anti_spam_led.off()






#new function to handle spamming
def checkstatus():
    if anti_spam_led.on():
        pass
    else:
        anti_spam_led.on()
        greenman() 

#create a function for greenman
def greenman():
    tl_green.off()
    tl_amber.blink(on_time=.5, off_time=.5,n=5)
    sleep(5)
    tl_red.on()
    
    
    
    red_led.off()
    green_led.on()
    sleep(10)
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
    
    tl_red.off()
    tl_green.on()
    #reset anti_spam_led
    anti_spam_led.off()
    

#logic of program
#set initial status of traffic light and pedestrian crossing
#start point
#traffic light is green and traffic is moving
tl_green.on()
#pedestrian crossing is red, cannot cross
red_led.on()

# some modification is needed here
#instead of running greenman, we run the check_status first
#pc_button.when_pressed = greenman
pc_button.when_pressed = checkstatus

pause()

