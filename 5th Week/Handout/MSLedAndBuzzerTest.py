from gpiozero import MotionSensor, LED, Buzzer
from signal import pause
from time import sleep

motion_detector = MotionSensor(4)
red_led = LED(12)


buzz = Buzzer(16)
buzz.off()

def alarm():
    buzz.blink(on_time=.5,off_time=.5,n=5)
    red_led.blink(on_time=.5,off_time=.5,n=5)
    sleep(5)
    

def alarmOff():
    buzz.off()
    red_led.off()
    


motion_detector.when_motion= alarm
motion_detector.when_no_motion = alarmOff
pause