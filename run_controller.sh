#!/usr/bin/bash
clear;
if [ `ps -e -o comm | grep pigpiod` == "pigpiod" ]
then
    sudo pigpiod;
fi
clear;
./controller.py &
