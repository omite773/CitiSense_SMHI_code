import subprocess
import os
from time import sleep

subprocess.call("sudo cp /home/pi/citisense/dhcpcd_ap.conf /etc/dhcpcd.conf",shell=True)
sleep(1)
subprocess.call("sudo cp /home/pi/citisense/interfaces_ap /etc/network/interfaces",shell=True)


