#Start sequence, carefully timed
#sudo umount /media/pi/KINGSTON/ &
#sleep 2
sudo sh /home/pi/citisense/hub-on.sh &
sleep 7
sudo hciconfig hci0 name 'Citisense_smhi'
sudo hciconfig hci0 noauth
sleep 1
sudo hciconfig hci0 piscan
sleep  1
sudo sdptool add SP
sudo python /home/pi/citisense/logger.py &
sleep 2
sudo python3 /home/pi/citisense/wireless_handler.py &
sleep 1
sudo sdptool add SP
sleep 1
#sudo hciconfig hci0 leadv 0
#iptables-restore < /home/pi/citisence/iptables.ipv4.nat
sleep 2
sudo sdptool add SP
