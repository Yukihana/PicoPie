from machine import Pin

led = Pin(16,Pin.OUT)
oled = Pin(25,Pin.OUT)

btn = Pin(0,Pin.IN,Pin.PULL_UP)
ledstate = False
btnlast = 0
btnread = 0

while True:
    btnread = btn.value()
    
    if btnread == 1 and btnread != btnlast:
        ledstate = not ledstate
        btnlast = btnread
    elif btnread == 0:
        btnlast = 0
    
    if ledstate:
        led.high()
        oled.low()
    else:
        led.low()
        oled.high()