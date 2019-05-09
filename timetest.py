import i2c2
import time
import subprocess
import sys

clock = i2c2.DS1307()
global month,dayOfMonth,hour,minute,second


try:
    clock.getTime()
    print clock.hour, ":", clock.minute, ":", \
    clock.second, " ", clock.dayOfMonth, "/", \
    clock.month, "/", clock.year,"  ", "weekday", \
    ":", clock.dayOfWeek 
    if(clock.month == 1):
        month = "JAN"
    elif(clock.month == 2):
        month = "FEB"
    elif(clock.month == 3):
        month = "MAR"
    elif(clock.month == 4):
        month = "APR"
    elif(clock.month == 5):
        month = "MAY"
    elif(clock.month == 6):
        month = "JUN"
    elif(clock.month == 7):
        month = "JUL"
    elif(clock.month == 8):
        month = "AUG"
    elif(clock.month == 9):
        month = "SEP"
    elif(clock.month == 10):
        month = "OCT"
    elif(clock.month == 11):
        month = "NOV"
    elif(clock.month == 12):
        month = "DEC"
    temp = str(clock.dayOfMonth) + " " + str(month) + " 20"+str(clock.year) + " " + str(clock.hour) +":"+str(clock.minute)+":00'"
    subprocess.call( "sudo date  -s '" + temp ,shell=True)
except IOError:
    print "IOERRRORRORORRORO"

print("Tesst")

