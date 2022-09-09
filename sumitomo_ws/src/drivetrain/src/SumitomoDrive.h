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

        // Methods        
        virtual void OnInit();


    public:
        // Constructor:
        Smartris(/* args */);

        // Destructor
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