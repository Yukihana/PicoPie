import time
from machine import Pin, PWM

pwm = PWM(Pin(16))
pwm.freq(15)

# Fade the LED in and out a few times.
duty = 0
direction = 2

while True:
    duty += direction
    if duty > 255:
        duty = 255
        direction = -2
    elif duty < 0:
        duty = 0
        direction = 2
        
    pwm.duty_u16(duty * duty)
    time.sleep(0.005)        