#!/usr/bin/bash

demon=`ps -e -o comm | grep pigpiod`
clear;
if [ "$demon" != "pigpiod" ]; then
    sudo pigpiod;
fi
clear;
./test.py &
