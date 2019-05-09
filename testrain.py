import rain
import RPi.GPIO as GPIO
import time

newCount = 0
rain.setup()
timer = 10000
while 1:
    newCount = rain.returnCount()
    print(newCount)
    time.sleep(5)

