import time
from machine import Pin, PWM

# Register pins
R = PWM(Pin(13))
G = PWM(Pin(12))
B = PWM(Pin(11))
R.freq(60)
G.freq(60)
B.freq(60)

# Data
# Subphase color combinations tied directly to LED pins: 012, 021, 120, 102, 201, 210
pincfg = [[R,G,B], [R,B,G], [G,B,R], [G,R,B], [B,R,G], [B,G,R]]
# Blink color composites ( Red = 1, Green = 2, Blue = 4, [Deprecated]Black = 0 )
blinkcfg = 1,2,4,1,2,4,1,2,4,1,2,4,3,6,5,3,6,5,3,6,5,3,6,5
# Sleep durations
SLEEP_BLINK = 0.15
SLEEP_PWM0 = 0.001
SLEEP_PWM1 = 0.001
SLEEP_BLACK = 0.2
SLEEP_WHITE = 0.5

# Temp
# Phase 0 & 1
pinproxy = dict([(0, pincfg[0][0]), (1, pincfg[0][1]), (2, pincfg[0][2])])
duty = dict([(0, 255), (1, 255), (2, 255)])
resetsp = True
direction = True
cfgindex = 0
# Phase 2
blinkindex = 0
blinktemp = 0
blinkon = False
# Compositing
animationphase = 0
phaseinitialized = False



# The infamous loop
while True:
    
    # Phase 0 - Fade
    if animationphase == 0:
        
        # Initialize phase
        if not phaseinitialized:
            for i in range(3):
                pinproxy[i] = pincfg[0][i]
                duty[i] = 255
            phaseinitialized = True
        
        # Extra freezzZ on white before changing values
        if resetsp:
            time.sleep(0.5)
            resetsp = False
        
        # Keyframe detection and execution
        if duty[0] <= 0 and duty[1] <= 0 and duty[2] <= 0:
            
            # Update index
            cfgindex += 1
            if cfgindex > 5:
                cfgindex = 0
                animationphase = 1
                phaseinitialized = False
            
            # Update target pins and initialize subphase
            resetsp = True
            for i in range(3):
                duty[i] = 255
                pinproxy[i] = pincfg[cfgindex][i]
            
            # Extra freezzZ on black
            time.sleep(SLEEP_BLACK)
        
        else:
            # Render frame
            if duty[0] > 0:
                duty[0] -= 1
            elif duty[1] > 0:
                duty[1] -= 1
            elif duty[2] > 0:
                duty[2] -= 1
            
        # Display frame
        for i in range(3):
            pinproxy[i].duty_u16(duty[i] * duty[i])
        
        # Inter-frame sleep
        time.sleep(SLEEP_PWM0)
        
    
    
    # Phase 1 - Wave
    elif animationphase == 1:
        
        # Initialize phase
        if not phaseinitialized:
            for i in range(3):
                pinproxy[i] = pincfg[0][i]
                duty[i] = 0
            phaseinitialized = True
        
        # Direction : Positive
        if direction:
            
            # Render frame
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
            
            # Render frame
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
                    animationphase = 2
                    phaseinitialized = False
                
                # Reroute pins on subphase change
                for i in range(3):
                    pinproxy[i] = pincfg[cfgindex][i]
            
                # Extra freezzZ on black
                time.sleep(0.2)
            
        # Display frame
        for i in range(3):
            pinproxy[i].duty_u16(duty[i] * duty[i])
        
        # zzZ
        time.sleep(SLEEP_PWM1)
    
    
    
    # Phase 2 - Blink
    else:
        
        # Initialize phase
        if not phaseinitialized:
            for i in range(3):
                pinproxy[i] = pincfg[0][i]
            phaseinitialized = True
        
        # Toggle subphase mode
        blinkon = not blinkon
        
        # Blink - OFF Default
        for i in range(3):
            duty[i] = 0
        
        # Blink - ON
        if blinkon:
            
            # Render frame
            blinktemp = blinkcfg[blinkindex]
            if blinktemp / 4 >= 1:
                duty[0] = 255
            blinktemp = blinktemp % 4
            if blinktemp / 2 >= 1:
                duty[1] = 255
            if blinktemp % 2 >= 1:
                duty[2] = 255 
            
            # Switch to next state
            blinkindex += 1
        
        elif blinkindex >= 24:
            blinkindex = 0
            animationphase = 0
            phaseinitialized = False
                
        # Display frame
        for i in range(3):
            pinproxy[i].duty_u16(duty[i] * duty[i])
        
        # zzZ
        time.sleep(SLEEP_BLINK)
