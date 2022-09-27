# URDF
Universal Robot Description File.

A file that contains information about the robot physical structure. Remember using Denavit Hartenberg standart to describe your robot.

## Tips:
* Group all your URDF files under myPackage/urdf/
* Parse your file once you think you've finished. This is to verify it has the correct syntax 
* Follow the [guide](http://wiki.ros.org/urdf/Tutorials/Create%20your%20own%20urdf%20file)!
* See more about [joints](http://wiki.ros.org/urdf/XML/joint) an their [description](https://ocw.tudelft.nl/course-lectures/2-2-1-introduction-to-urdf/)
* See hoe the reference frame are affected by each tag [in](https://abedgnu.github.io/Notes-ROS/chapters/ROS/10_robot_modeling/urdf.html#link)


## Minor dependencies:
* If you haven't, install `sudo apt-get install liburdfdom-tools`
* Use `check_urdf myFile.urdf`

## Remeber:
* URDF and, on it's own xml files are not that modular, which goes against all of the coding principles! 
* Xacros are the default when it comes to implementing modules, parameters, and even math into XML files
* It's a good idea to also separate your xacros, make them readable
* If you try to implement a **URDF** file with macros, you'll successfully fail. Tho, you can convert the xacro URDF-ish to a real URDF with the command `rosrun xacro xacro pan_tilt.xacro > pan_tilt_generated.urdf` 
    * Alternatively, add it to your build
    * NOTE: Before running the command, source devel/setup.bash

## ROS Control

If you would like to use a ROS controller, it should be enough to add transmission into the robot's URDF file, however, I recommend using Gazebo_ROS_Control because it has more [documentation](https://classic.gazebosim.org/tutorials?tut=ros_control&cat=connect_ros) on it. 
    