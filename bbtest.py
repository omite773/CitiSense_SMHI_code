import i2c_bb_devices


#Initiate availabilities for plugNplay functionality
ccs811_available = False
mic_available = False
display_available = False
adc_available = False
arduino_available = False
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

mode = 0x10
# mode: 0x10 = 1_sec_meas, 0x00 idle, 0x20 10_sec_meas, 0x30 60_sec_meas
res = i2c_bb_devices.init_ccs811(mode)
print(res)
if(res):
    #Init returns 2 if newly booted and should wait 20min before accurate read
    #Not finnished implementing yet though
    global ccs811_available
    ccs811_available = True
if(i2c_bb_devices.arduino_init()):
    global arduino_available
    arduino_available = True

res = i2c_bb_devices.init_ccs811(mode)
print(res)
print(ccs811_available)
print(arduino_available)
(co, tvc) = i2c_bb_devices.read_gas()
print(co)
print(tvc)


i2c_bb_devices.checkerror()



