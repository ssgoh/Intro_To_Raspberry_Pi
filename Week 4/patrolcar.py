from machine import Pin
import utime


button=Pin(13,Pin.IN,Pin.PULL_DOWN)
red_led = Pin(16,Pin.OUT)
blue_led = Pin(17,Pin.OUT)
buzz = Pin(15,Pin.OUT)
#buzzer = machine.Pin(14,machine.Pin.OUT)
buzz.off()
while True:
    print(button.value())
    if button.value() == 1:
        print('high')
        red_led.on()
        
        buzz.on()
        for x in range(1,10,1):
            red_led.on()
            blue_led.off()
            utime.sleep(.2)
            red_led.off()
            blue_led.on()
            utime.sleep(.2)
            
        red_led.off()
        blue_led.off()
        buzz.off()
    else:
        red_led.low()
        blue_led.low()
        buzz.off()