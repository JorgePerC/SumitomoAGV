#!/bin/bash

bitrate=500000
echo "Setting CAN bus Up"

echo "Bitrate is: $bitrate"
sudo modprobe can
sudo modprobe can_raw
sudo modprobe mttcan

sudo ifconfig can0 txqueuelen 10000

echo "Services are up"

sudo ip link set can0 type can bitrate $bitrate 

sudo ip link set can0 up

