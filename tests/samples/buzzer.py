#
# This file plays the buzzer
#   using random sounds.
#
import time
from time import sleep
from machine import Pin, PWM
from random import choice, randint

# freqs = [440,880, 1024,2048, 550, 1200]

# Get a list of frequencies.
freqs = [32, 36, 41, 43, 49, 55, 61]

# Send current to pin 27.
p = Pin(27, Pin.OUT)

# Use the Pulse Width Modulation
#   to create analog signals.
b = PWM(p)
b.deinit()
b.init()

t = 1
try:
    # Play for 30 seconds.
    for _ in range(30):
      for f in freqs:
        b.duty(1000)
        b.freq(8*f)
        # t = randint(1, 10)/100.0
        sleep(t) 
finally:
    print("Teardown")
    b.duty(0)
    b.deinit()
