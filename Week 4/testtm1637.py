#Library
import utime
import tm1637


#setup
tm = tm1637.TM1637(clk=machine.Pin(4), dio=machine.Pin(5))

#to clear the display
tm.show('    ')
utime.sleep(2)

#to present data on the display
#here are the examples
tm.number(1)
utime.sleep(2)
tm.number(12)
utime.sleep(2)
tm.number(123)
utime.sleep(2)
tm.number(1234)
utime.sleep(2)
#notice that the display starts from right to left

#to display time with the colon seperating hour and minutes
tm.numbers(12,30,True)


#digital clock
while True:
    time=utime.localtime()
    print(time)
    #(2023, 2, 6, 20, 14, 57, 0, 37)
    #   0   1  2   3   4   5  6   7
    hr=time[3]
    mn=time[4]
    tm.numbers(hr,mn,True)
    utime.sleep(60)


#if you open up tm1637.py you can see the functions number() and numbers()
#in this library
