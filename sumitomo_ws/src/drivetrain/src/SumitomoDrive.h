// ROS includes
#include <ros/ros.h>
#include <ros/time.h>
#include <nodelet/nodelet.h>
#include <std_msgs/String.h>


// Plugin (also needed for nodelets)
#include <pluginlib/class_list_macros.h>
#include <pluginlib/class_loader.h>

#ifndef SUMITOMO_H
#define SUMITOMO_H

/*
Declaration for class Smartris
*/

namespace SumitomoDrive{

    class Smartris : public nodelet::Nodelet {
    private:
        // Arguments
        int nodeID;
        bool isForward;

        // ROS
        ros::Publisher pub;
        ros::Subscriber sub;

        // Methods        
        virtual void onInit();


    public:
        // Constructor:
        // We don't need to rewrite the constructor. We can just use the default one.
        // Smartris(ros::NodeHandle * nh);
        // Smartris();


        // Destructor   
        // Same as with the constructor. We don't need to rewrite it.
        //virtual ~Smartris();

        void setVelocity();
        void setMaxVelocity();
        void setDirection();

        void setOperationStatus();

    };


} // namespace name


#endif /* SUMITOMO_H*/

// Process the class as a nodelet
PLUGINLIB_EXPORT_CLASS(SumitomoDrive::Smartris, nodelet::Nodelet)
//PLUGINLIB_EXPORT_CLASS(drivetrain, Smartris, SumitomoDrive::Smartris, nodelet::Nodelet)