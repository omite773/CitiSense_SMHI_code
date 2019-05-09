import os

trash = ""
character = ""

file = open("/home/pi/citisense/logs/data_log.csv")
for line in file:
    for word in line:
        if (word.endswith(",")):
            trash += word
        elif (word.endswith("\n")):
            character += " "
        else:
            character += word
char_array = character.split(' ')

lines = int(((len(char_array)-1)/11)-1)
temp_array = [None] * int(lines)


for i in range(lines):
    temp_array[i] = char_array[11+i*11:22+i*11]
for s in range(len(temp_array)):
    time = temp_array[s][0]
    tempC = temp_array[s][1]
    CO2 = temp_array[s][2]
    TVOC = temp_array[s][3]
    rain = temp_array[s][4]
    noise = temp_array[s][5]
    wind = temp_array[s][6]
    sun = temp_array[s][7]
    battery= temp_array[s][8]
    current= temp_array[s][9]
    watt = temp_array[s][10]
    sdata = {"sensid": "Citisense", "Time" : time, "Temp_C": tempC, "CO2_ppm": CO2, "TVOC_ppb": TVOC, "Rain_V": rain, "Noise_dBV": noise, "Wind_mV": wind, "Sun_V": sun, "Battery_V": battery, "Current_mA": current, "Watt_mW": watt}
    print(sdata)

  
        
          


        
    