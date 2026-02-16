#BANAT SINGH
from machine import Pin,PWM

import time 

led1 = Pin(5, Pin.OUT)
led2 = Pin(18, Pin.OUT)
led3 = Pin(19, Pin.OUT)
led4 = Pin(21, Pin.OUT)

while True :

    # ANTI-CLOCKWISE 
    for i in range(2000):
        led4.on()
        led3.off()
        led2.off()
        led1.off()
        time.sleep(0.005)

        led4.off()
        led3.on()
        led2.off()
        led1.off()
        time.sleep(0.005)
        
        led4.off()
        led3.off()
        led2.on()
        led1.off()
        time.sleep(0.005)

        led4.off()
        led3.off()
        led2.off()
        led1.on()
        time.sleep(0.005)

        
    time.sleep(0.2)

    # CLOCKWISE 
    for i in range(2000):

        led4.off()
        led3.off()
        led2.off()
        led1.on()
        time.sleep(0.005)

        led4.off()
        led3.off()
        led2.on()
        led1.off()
        time.sleep(0.005)

        led4.off()
        led3.on()
        led2.off()
        led1.off()
        time.sleep(0.005)

        led4.on()
        led3.off()
        led2.off()
        led1.off()
        time.sleep(0.005)

    # gap
    time.sleep(0.2)
