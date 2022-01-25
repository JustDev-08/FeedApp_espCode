from machine import Pin, PWM
import time


servo1 = PWM(Pin(4), freq=50, duty=100)
servo1.duty(30)
time.sleep(3)