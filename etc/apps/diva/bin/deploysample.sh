#!/bin/sh
rm -rf /home/pi/diva
mkdir /home/pi/diva
cp -rf ./diva /home/pi/
cp -f ./grovepi.py /home/pi/diva/assignment_3
sudo chown -R pi: /home/pi/diva
echo Diva example codes copied to /home/pi/
