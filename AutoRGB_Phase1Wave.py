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
direction = True
pinproxy = dict([(0, pincfg[0][0]), (1, pincfg[0][1]), (2, pincfg[0][2])])
duty = dict([(0, 0), (1, 0), (2, 0)])



# The infamous loop
while True:
    
    # Direction : Positive
    if direction:
        
        # Frame render
        if duty[0] < 255:
            duty[0] += 1
        elif duty[1] < 255:
            duty[1] += 1
        elif duty[2] < 255:
            duty[2] += 1
    
        # Keyframe detection and reversal
        if duty[0] >= 255 and duty[1] >= 255 and duty[2] >= 255:
            direction = False
            
    # Direction : Negative
    else:
        
        # Frame render
        if duty[0] > 0:
            duty[0] -= 1
        elif duty[1] > 0:
            duty[1] -= 1
        elif duty[2] > 0:
            duty[2] -= 1
            
        # Keyframe detection and subphase change
        if duty[0] <= 0 and duty[1] <= 0 and duty[2] <= 0:
            direction = True
            
            cfgindex += 1
            if cfgindex > 5:
                cfgindex = 0
            
            # Reroute pins on subphase change
            pinproxy[0] = pincfg[cfgindex][0]
            pinproxy[1] = pincfg[cfgindex][1]
            pinproxy[2] = pincfg[cfgindex][2]
        
            # Extra freezzZ on black
            time.sleep(0.2)
        
    # Frame display
    pinproxy[0].duty_u16(duty[0] * duty[0])
    pinproxy[1].duty_u16(duty[1] * duty[1])
    pinproxy[2].duty_u16(duty[2] * duty[2])
    
    # zzZ
    time.sleep(0.001)