# Config folder

According to Joseph Lentin, 2018

config: All configuration files that are used in this ROS package are kept in this folder. This folder is created by the user and it is a common practice to name the folder config as this is where we keep the configuration files.


## Description:

| File  | What for |
|-------|----------|
| can.yaml      | CAN port configuration file |
| motor*.yaml   | Node description file  |
| controller.yaml   | Parameters for initialing motor controllers, which can be implemented virturally or physically |

According to what I've read, we need the different configuration files to control physically the robot, even tho we might not be simulating anything. 

References:

https://sir.upc.edu/projects/rostutorials/10-gazebo_control_tutorial/index.html#hardware-abstraction-layer
