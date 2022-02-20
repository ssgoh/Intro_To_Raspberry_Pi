from gpiozero import MotionSensor, LED, Buzzer, Button
from signal import pause
from time import sleep

motion_detector = MotionSensor(4)
red_led = LED(12)

armed_led=LED(20)
armed_led.off()

arm_button=Button(2)
reset_button=Button(21)

buzz = Buzzer(16)
buzz.off()

def alarm():
    red_led.blink(on_time=.5,off_time=.5,n=20)
    buzz.blink(on_time=.5,off_time=.5,n=20)
    sleep(20)

def armAlarm():
    armed_led.on()
    motion_detector.when_motion = alarm
    
def disarmAlarm():
    armed_led.off()
    buzz.off()
    red_led.off()
    motion_detector.when_motion = None
    
    



arm_button.when_pressed = armAlarm
reset_button.when_pressed = disarmAlarm

while True:
    pause()