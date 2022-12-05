from machine import Pin
import time

led = Pin(16,Pin.OUT)
led2 = Pin(25,Pin.OUT)

wait = 0.16
direction = False
waitMax = 0.32
waitMin = 0.02
waitDelta = 0.02

while True:
    if direction == True:
        wait += waitDelta
        if wait >= waitMax:
            wait = waitMax
            direction = False
    else:
        wait -= waitDelta
        if wait <= waitMin:
            wait = waitMin
            direction = True
    
    led.high()
    led2.low()
    time.sleep(wait)
    led.low()
    led2.high()
    time.sleep(wait)
    