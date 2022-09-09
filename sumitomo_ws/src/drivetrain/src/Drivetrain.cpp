#include <ros/ros.h>

#include <stdlib.h>

// Import Messages, remember to add them to the Cmakelist.txt
#include "std_msgs/String.h"
#include <geometry_msgs/Twist.h>


int main(int argc, char *argv[])
{

    // Initialize ROS node  
    ros::init(argc, argv, "drivetrain");

    // Communication handler for node. 
    // It basically starts a node
    ros::NodeHandle n;
    

    // Define iterations per second
    ros:: Rate rate(10)

    return 0;
}
