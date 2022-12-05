from machine import Pin
from time import sleep

ledindex = 0
direction = True
sleeptime = 0.05

# Register LED pins
led0 = Pin(0,Pin.OUT)
led1 = Pin(2,Pin.OUT)
led2 = Pin(5,Pin.OUT)
led3 = Pin(7,Pin.OUT)
led4 = Pin(10,Pin.OUT)

while True:
    
    # Rotation Logic
    if direction:
        ledindex += 1
    else:
        ledindex -= 1
    if ledindex == 0 or ledindex == 4:
        direction = not direction
    
    # Update LED Array
    led0.high() if ledindex == 0 else led0.low()
    led1.high() if ledindex == 1 else led1.low()
    led2.high() if ledindex == 2 else led2.low()
    led3.high() if ledindex == 3 else led3.low()
    led4.high() if ledindex == 4 else led4.low()
    
    # Cycle timer
    sleep(0.05)