import time
from machine import Pin, PWM

# Register pins
R = PWM(Pin(13))
G = PWM(Pin(12))
B = PWM(Pin(11))
R.freq(60)
G.freq(60)
B.freq(60)

# Subphase color combination data tied directly to LED pins: 012, 021, 120, 102, 201, 210
pincfg = [[R,G,B], [R,B,G], [G,B,R], [G,R,B], [B,R,G], [B,G,R]]

# Temporary variables
cfgindex = 0
resetsp = True
pinproxy = dict([(0, pincfg[0][0]), (1, pincfg[0][1]), (2, pincfg[0][2])])
duty = dict([(0, 255), (1, 255), (2, 255)])



# The infamous loop
while True:
    
    # Extra freezzZ on white before changing values
    if resetsp:
        time.sleep(0.5)
        resetsp = False
    
    # Keyframe detection and execution
    if duty[0] == 0 and duty[1] == 0 and duty[2] == 0:
        
        # Reset
        resetsp = True
        duty[0] = 255
        duty[1] = 255
        duty[2] = 255
        
        # Update index
        cfgindex += 1
        if cfgindex > 5:
            cfgindex = 0
        
        # Update target pins
        for i in range(3):
            pinproxy[i] = pincfg[cfgindex][i]
        
        # Extra freezzZ on black
        time.sleep(0.2)
    
    # Frame render
    if duty[0] > 0:
        duty[0] -= 1
    elif duty[1] > 0:
        duty[1] -= 1
    elif duty[2] > 0:
        duty[2] -= 1
        
    # Frame display
    for i in range(3):
        pinproxy[i].duty_u16(duty[i] * duty[i])
    
    # Inter-frame sleep
    time.sleep(0.001)