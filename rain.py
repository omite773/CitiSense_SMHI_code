import RPi.GPIO as GPIO


count = 0

def isr(channel):
    global count
    count += 0.288

def returnCount():
    global count
    return count

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(11, GPIO.FALLING, callback = isr, bouncetime = 100)


def resetCount():
    global count
    count = 0 
