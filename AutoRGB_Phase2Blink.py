from machine import Pin
from time import sleep

# Register LED pins
R = Pin(13,Pin.OUT)
G = Pin(12,Pin.OUT)
B = Pin(11,Pin.OUT)

# Blink data composite ( Red = 1, Green = 2, Blue = 4 )
blinkcfg = 1,2,4,1,2,4,1,2,4,1,2,4,3,6,5,3,6,5,3,6,5,3,6,5
blinkindex = 0
blinksleep = 0.15

# Temporary variables
blinktemp = 0
blinkon = False

while True:
    
    # Toggle subphase mode
    blinkon = not blinkon
    
    # Blink - ON
    if blinkon:
        
        # Render frame
        blinktemp = blinkcfg[blinkindex]
        B.high() if blinktemp / 4 >= 1 else B.low()
        blinktemp = blinktemp % 4
        G.high() if blinktemp / 2 >= 1 else G.low()
        R.high() if blinktemp % 2 >= 1 else R.low()
        
        # Switch to next state
        blinkindex += 1
        if blinkindex >= 24:
            blinkindex = 0
    
    # Blink - OFF
    else:
        
        R.low()
        G.low()
        B.low()
    
    # zzZ
    sleep(blinksleep)