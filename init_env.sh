#!/bin/bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python python-dev sqlite3 vnstat git htop nginx 
if [ -f /usr/local/bin/pip ] || [ -f /usr/bin/pip ];
then
    echo "pip exists"
else
    echo "Installing pip"
    wget https://bootstrap.pypa.io/get-pip.py
    sudo python get-pip.py
fi
echo "init vnstat to monitor network"
sudo vnstat -u -i eth0
sudo chown -R vnstat:vnstat /var/lib/vnstat
echo "install fabric for remote cmd"
sudo pip install fabric


