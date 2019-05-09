import os
import time
import math
import subprocess
import sys
from time import sleep
from datetime import datetime
import rtc #Library for RTC clock
#Sensordevices
import i2c_devices
import rain as regn

#Initiate availabilities for plugNplay functionality
temperature_available = False

#Keep sensor values global for ease of access
temp = None
co = None
tvoc = None
rain = None
mic = None
wind = None
sun = None
battery = None
current = None
watt = None
arduino_Vref = 5.0

local_const_timer = 100
usb_const_timer= 10

usb_timer = usb_const_timer
local_timer = local_const_timer



def rtcTime():
    #Update RPI clock with the RTC
    clock = rtc.DS1307()
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
        print "Could not getTime from the RTC"


#Figure out available devices at launch, also set certain settings
def initiate():

    if(i2c_devices.temp_init()):
        global temperature_available
        temperature_available = True

    
#Write current measurement values to the log file
def append_log():
    global temperature_available
    global temp
    global co
    global tvoc
    global rain
    global mic
    global wind
    global sun
    global battery
    global current
    global watt
    if os.path.isdir("/home/pi/citisense/logs/"):
        try:
            #Open log file
            file = open("/home/pi/citisense/logs/data_log.csv", "a")
        except IOError as e:
            #Some error logging
            print("IO-Err logger")
            log_error(str(e) + " Opening data_log.csv ERR")
            return 2

        if os.stat("/home/pi/citisense/logs/data_log.csv").st_size == 0:
            #If log file empty, fill out header
            file.write('Time, Temp[C], CO2[ppm], TVOC[ppm], Rain[V], Noise[dBV], Wind[mV], Sun[V], Battery[V], Current[mA], Watt[mW]\n')
        #Then the sensor values separated by commas (.csv-format)
        file.write(datetime.now().strftime('%Y-%m-%d_%H:%M') + ", " + str(temp) + ", " + str(co) + ", " + str(tvoc) + ", " + str(rain) + ", " + str(mic) + ", " + str(wind) + ", " + str(sun) + ", " + str(battery) + ", " + str(current) + ", " + str(watt) + "\n" )
        regn.resetCount()
        file.close()

def update_sensors(Log, Backup):
    #Specify globals
    global temperature_available
    global temp
    global co
    global tvoc
    global rain
    global mic
    global wind
    global sun
    global battery
    global current
    global watt

    if(temperature_available):
        try:
            rain = regn.returnCount()
            temp = i2c_devices.get_temperature()
        except Exception as e:
            #Catch sensor error and disable it
            temp = None
            temperature_available = False
            log_error(str(e) +  " TEMP_SENS ERR, disabling")
            
    if Log == True:
        #Log to local .csv file
        append_log()

    if Backup == True:
        #Backup all logs + picture to USBw
        #Run pic + copy scripts, return errors
        err += subprocess.call(['sudo', 'sh', '/home/pi/citisense/cp_to_usb.sh'])
        if err != 0:
            log_error(str(err) + " USB_mem or camera error")
            
def shutdown():
    #Shutdown procedure, closes buses and syncs OS to SD-card
    print("exiting")
    log_error("Shutting down due to low battery")
    i2c_devices.close_bus()
    subprocess.call(['sudo', 'sync'])
    subprocess.call(['sudo', 'shutdown', '-h', 'now'])
    sys.exit()

def log_error(e):
    #Error logging
    file = open("/home/pi/citisense/logs/error.txt", "a")
    file.write(datetime.now().strftime('%Y-%m-%d_%H:%M') + " Msg: " + e + "\n")
    file.close()

initiate()
regn.setup()
rtcTime()

#Store values locally every 200 seconds, and on USB 200*5 seconds
while(1):
    local_timer -=1
    if local_timer == 0:
        local_timer = local_const_timer
        print("logging...")
        if usb_timer == 0:
            update_sensors(True, True) #log USB
            usb_timer = usb_const_timer
        else:
            usb_timer -= 1
            update_sensors(True, False) #log local
    else:
        update_sensors(False, False)
    sleep(0.8)
