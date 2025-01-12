from time import sleep_ms, sleep
from board import LED
from machine import Pin, ADC

# Digital pins
button = Pin(21, Pin.IN, pull=Pin.PULL_UP)

# Analog Pins
x = Pin(4)
y = Pin(5)

while True:
  if not button.value():
    print("Stop!")
    break
  # You need to instantiate ADC every time to make it work:
  #   why?
  coord = [ADC(i).value() for i in (x,y)]
  print(coord)
  sleep_ms(100)
