# SumiyomoAGV
Base code for Sumitomos AGV, and companion app
## Glosary:
|Acronymn| Meaning |
|-------|-------|
CAN     | Controller Area Network |
CDM     | CANopen Device Monitor |
CiA     | CAN in Automation e.V. |
CMS     | CAN Message Specification |
COB     | Communication Object (CAN Message) |
COBID   | Communication Object Identifier |
CRC     | Cyclic redundancy check. Bit error protection method for data communication |
CSDO    | Client SDO |
DAM     | Destination Address Mode |
EDS     | Electronic Data Sheet. This is a file with the device specific parameter description and is provided by the manufacturer of a DeviceNet or CANopen device. |
EMCY    | Emergency Object |
HAL     | Hardware Abstraction Layer |
ISR     | Interrupt Service Routine |
LME     | Layer Management Entity |
LMT     | Layer Management |
LSS     | Layer Setting Services |
MPDO    | Multiplexed PDO |
NMT     | Network Management |
OD      | Object Dictionary |
PDO     | Process Data Objects. They are messages in an unconfirmed service. They are used for the transfer of real-time data to and from the device. |
RPDO    | Receive PDO |
RTR     | Remote Transmission Request |
SAM     | Source Address Mode |
SCT     | Safeguard Cycle Time (CANopen Safety) |
SDO     | Service Data Objects, messages in a confirmed service. They are used for the access of entries in the object dictionary. |
SRD     | SDO Requesting Device |
SRDO    | Safety Relevant Data Objects |
SRVT    | Safety Relevant object Validation Time (CANopen Safety) |
SSDO    | Server SDO |
SYNC    | Synchronization Object (CANopen communication object) |
TIME    | Time Stamp Object |
TPDO    | Transmit PDO

[Source](https://portgmbh.atlassian.net/wiki/spaces/CAL/pages/191627277/Glossary)

--------

## Ginkgo USB-CAN Interface Adapter

### Materials:

* Printer 2 USB cable
* Ginkgo CAN interface

### Set Up

1. Connect the driver to your computer
1. Use the terminal to list all your USB devices. Write down the device Bus XXX Device XXX and ID XXXX:XXXX (idVendor:idProduct)

    lsusb

1. On the host device, create a filename called **etc/udev/rules.d/10-GinkgoUSBCAN.rules**. 
    1. Write the following to the file:
    
    SUBSYSTEMS=="usb", ATTRS{idVendor}=="0483", ATTRS{idProduct}=="0666", GROUP="jpc"

    2. Take into account the idVendor and idProduct listed on your USB Devices. And also, change the group your user belongs to. 

    whoami

    groups


    3. [Source](https://www.clearpathrobotics.com/assets/guides/kinetic/ros/Udev%20Rules.html)
    4. [Source](https://www.linuxquestions.org/questions/blog/indymaynard-261967/viewtool-ginkgo-usb-can-interface-adapter-37419/)
1. Once you've done that, execute:, where the 0XX is replaced by the *Device* shown in the listed USB devices

    sudo udevadm info -a -p $(udevadm info -q path -n /dev/bus/usb/001/0XX)

1. After that a list of pci devices will be shown, look for the one that has as *manufacturer:* **ViewTool**. Copy it's device name, it's quotated. Mine is: ``'/devices/pci0000:00/0000:00:08.1/0000:05:00.3/usb1/1-2'``

1. Test the device

    sudo udevadm test /devices/pci0000:00/0000:00:08.1/0000:05:00.3/usb1/1-2

1. If no errors are promted, you are good to go
1. Wake up the CAN service [Source](https://elinux.org/Bringing_CAN_interface_up)

    sudo modprobe can-raw
    
    sudo modprobe slcan
    
    sudo slcand -o -s8 -t hw -S 3000000 /dev/ttyUSB0
    
    sudo ip link set up slcan0
1. Remember to set correctly the transmission bitrate

SCII Command| CAN Bitrate
------------|------------
s0 | 10 Kbit/s
s1 | 20 Kbit/s
s2 | 50 Kbit/s
s3 | 100 Kbit/s
s4 | 125 Kbit/s
s5 | 250 Kbit/s
s6 | 500 Kbit/s
s7 | 800 Kbit/s
s8 | 1000 Kbit/s
------
### Install drivers:
1. Go to the following website: http://viewtool.com/product/readmefirst/
1. Choose the file for your architecture and OS, then download it.
    1. As you decompress it, you'll realice it's a library object. ``file.so`` on Linux. 
    1. Save it under the /lib or /usr/lib folder, with a name that's easily recallable. I chose to create the folder viewtool_CAN, and moved the files there
    1. [Source](https://www.systranbox.com/where-are-so-files-stored-in-linux/)
1. Download the bootloader from the first link and make sure the driver was installed correctly
1. Download [SocketCAN](http://www.viewtool.com/index.php/en/22-2016-07-29-02-11-32/308-ginkgo-socketcan-software-download)
    1. Since the file is a ``file.ko``, that basically means it's a loadable kernel module
    1. Follow this [document](http://www.viewtool.com/demo/Ginkgo/Documents/GinkgoSocket%20CAN%20Application%20Note%20v1.0.pdf) to complete the installation
1. Download the library for the language you'll be using from 


    modinfo first_driver.ko 
    
    uname -r

    dmesg | tail


https://manpages.ubuntu.com/manpages/bionic/man1/slcand.1.html

https://scratchrobotics.com/2019/07/03/how-to-enable-can-bus-on-nvidia-jetson-tx2-developer-board/


---------------------
### Turn on fans:
sudo jetson_clocks

sudo echo 255 > /sys/devices/pwm-fan/target_pwm

### SSH

The SSH deamon is on by default on the Jetson

ssh-keygen

Codesys Edge Gateway
Codesys control (CAN)