from machine import Pin, PWM
from time import sleep

ledindex = 0
direction = True
sleeptime = 0.2

# Register LED pins
led0 = Pin(11,Pin.OUT)
led1 = Pin(12,Pin.OUT)
led2 = Pin(13,Pin.OUT)
led3 = Pin(18,Pin.OUT)
led4 = Pin(19,Pin.OUT)
led5 = Pin(20,Pin.OUT)

while True:
    
    # Rotate
    if direction:
        ledindex += 1
    else:
        ledindex -= 1
    if ledindex == 0 or ledindex == 5:
        direction = not direction
    
    # Update LED Array
    led0.high() if ledindex == 0 else led0.low()
    led1.high() if ledindex == 1 else led1.low()
    led2.high() if ledindex == 2 else led2.low()
    led3.high() if ledindex == 3 else led3.low()
    led4.high() if ledindex == 4 else led4.low()
    led5.high() if ledindex == 5 else led5.low()
    
    # Cycle timer
    sleep(sleeptime)
