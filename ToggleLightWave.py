import _thread
from machine import Pin
from time import sleep

# For alt thread
def LedCycle():
    from machine import Pin
    import time
    
    ledindex = 0
    
    # Register LED pins
    led0 = Pin(0,Pin.OUT)
    led1 = Pin(4,Pin.OUT)
    led2 = Pin(7,Pin.OUT)
    led3 = Pin(10,Pin.OUT)
    led4 = Pin(14,Pin.OUT)
    
    while True:
    # LED Output
    # if ledstate:
        
        # Rotate
        ledindex += 1
        if ledindex > 4:
            ledindex = 0
        
        # Update
        led0.high() if ledindex == 0 else led0.low()
        led1.high() if ledindex == 1 else led1.low()
        led2.high() if ledindex == 2 else led2.low()
        led3.high() if ledindex == 3 else led3.low()
        led4.high() if ledindex == 4 else led4.low()
        
        # Cycle timer
        time.sleep(0.2)

_thread.start_new_thread(LedCycle,())

# For main thread
btn = Pin(26,Pin.IN,Pin.PULL_UP)
oled = Pin(25,Pin.OUT)
opstate = False
ledstate = False

btnlast = 0
btnread = 0

while True:
    btnread = btn.value()
    
    # Toggle state on button press
    if btnread == 1 and btnread != btnlast:
        ledstate = not ledstate
        if ledstate:
            oled.high()
        else:
            oled.high()
        btnlast = btnread
    elif btnread == 0:
        btnlast = 0
    
    
        
