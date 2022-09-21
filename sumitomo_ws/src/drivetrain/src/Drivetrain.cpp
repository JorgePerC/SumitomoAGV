#include <ros/ros.h>
#include <stdlib.h>

#include "std_msgs/String.h"
#include <geometry_msgs/Twist.h>

// ++Plugin imports
#include <boost/shared_ptr.hpp> 
#include <pluginlib/class_list_macros.h>

// ROS Control imports
#include <controller_manager/controller_manager.h>
#include <controller_interface/controller.h>
#include <hardware_interface/joint_command_interface.h>
//#include "SumitomoDrive.h"

int main(int argc, char *argv[])
{

    // Initialize ROS node  
    ros::init(argc, argv, "drivetrain");

    // Communication handler for node. 
    // It basically starts a node
    ros::NodeHandle nh;
    
    //SumitomoDrive::Smartris motor1 (); //

    // Define iterations per second
    ros:: Rate rate(10);

    // TODO: Initialize ros CANOpen   
        //Does it have a plugin??     
 
    ros::spin();

    return 0;
}
