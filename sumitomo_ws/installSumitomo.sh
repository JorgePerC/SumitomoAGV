#!/bin/sh

# ======= ZED wrapper =======

echo "Cloning ZED grapper"


cd src
git clone --recursive https://github.com/stereolabs/zed-ros-wrapper.git
cd ../
rosdep install --from-paths src --ignore-src -r -y
catkin_make -DCMAKE_BUILD_TYPE=Release
source ./devel/setup.bash


# ===== CANOpen packages ====
echo "Installing canOpen packages..."

sudo apt install ros-$(echo $ROS_DISTRO)-socketcan-interface
sudo apt install ros-$(echo $ROS_DISTRO)-socketcan-bridge
sudo apt install ros-$(echo $ROS_DISTRO)-canopen-*


# ===== RQT ==========
echo "Installing RQT packages"
sudo apt-get install ros-melodic-rqt ros-melodic-rqt-common-plugins ros-melodic-rqt-robot-plugins
