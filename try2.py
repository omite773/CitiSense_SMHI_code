import csv


result =list(csv.reader(open("/home/pi/citisense/logs/data_log.csv")))

counter = 0
for s in result[1:]:
    time = s[0]
    tempC = s[1]
    CO2 = s[2]
    TVOC = s[3]
    rain = s[4]
    noise = s[5]
    wind = s[6]
    sun = s[7]
    battery= s[8]
    current= s[9]
    watt = s[10]
    sdata = {"sensid": "Citisense", "Time" : time, "Temp_C": tempC, "CO2_ppm": CO2, "TVOC_ppb": TVOC, "Rain_V": rain, "Noise_dBV": noise, "Wind_mV": wind, "Sun_V": sun, "Battery_V": battery, "Current_mA": current, "Watt_mW": watt}
    if(counter< 5):
        print(sdata)
    counter +=1

filename = "/home/pi/citisense/logs/data_log2.csv"
f = open(filename,"w+")

f.write('Time, Temp[C], CO2[ppm], TVOC[ppm], Rain[V], Noise[dBV], Wind[mV], Sun[V], Battery[V], Current[mA], Watt[mW]\n')
f.close

