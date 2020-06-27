#!/bin/bash


#for RPiPlay

sudo apt-get install cmake
sudo apt-get install libavahi-compat-libdnssd-dev
sudo apt-get install libssl-dev

#for lazycast
 
wget http://ftp.us.debian.org/debian/pool/main/w/wpa/wpasupplicant_2.4-1+deb9u4_armhf.deb
sudo apt --allow-downgrades install ./wpasupplicant_2.4-1+deb9u4_armhf.deb
sudo apt install network-manager network-manager-gnome openvpn openvpn-systemd-resolved network-manager-openvpn network-manager-openvpn-gnome
sudo apt purge dhcpcd5
sudo systemctl disable systemd-resolved
sudo reboot

#for web&db

pip install flask flask-sqlalchemy
sudo apt install gunicorn3
