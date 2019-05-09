
import i2c_devices
import time

i2c_devices.beginClock()
i2c_devices.setTimeTest(0,30, 2, 7, 4,5,6)
i2c_devices.startClock()
while(1):
    i2c_devices.getTime()
    print
    time.sleep(1)



