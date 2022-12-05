from machine import Pin
import time

led = Pin(16,Pin.OUT)

wait = 0.08

while True:
    led.high()
    time.sleep(wait)
    led.low()
    time.sleep(wait)
