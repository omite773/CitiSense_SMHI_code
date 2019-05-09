sudo service hostapd stop
sudo systemctl start dhcpcd.service
sudo ifdown wlan0
sudo ifup wlan0
