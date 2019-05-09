import subprocess
import os
from time import sleep

subprocess.call("sudo cp /home/pi/citisense/dhcpcd_wifi.conf /etc/dhcpcd.conf",shell=True)
sleep(1)
subprocess.call("sudo cp /home/pi/citisense/interfaces_wifi /etc/network/interfaces",shell=True)


