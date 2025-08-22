from machine import Pin
import time
ledGreen = Pin(18, Pin.OUT)
ledGreen.value(1)
ledBlue = Pin(17, Pin.OUT)
ledBlue.value(1)
ledRed = Pin(16, Pin.OUT)
ledRed.value(1)
import random
from machine import Timer
def pickColor(value):
    if value is None:
        ledRed.value(1)                                     
        ledGreen.value(1)                                   
        ledBlue.value(1)
    else:
        ledRed.value(random.getrandbits(1))                                     
        ledGreen.value(random.getrandbits(1))                                   
        ledBlue.value(random.getrandbits(1))
timer = Timer()
timer.init(freq=2.5, mode=Timer.PERIODIC, callback=pickColor)
time.sleep(10)
timer.deinit()