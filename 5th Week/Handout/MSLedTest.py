from gpiozero import MotionSensor, LED, Buzzer
from signal import pause
from time import sleep

motion_detector = MotionSensor(4)
red_led = LED(12)


buzz = Buzzer(16)
buzz.off()


motion_detector.when_motion= red_led.on
motion_detector.when_no_motion = red_led.off
pause