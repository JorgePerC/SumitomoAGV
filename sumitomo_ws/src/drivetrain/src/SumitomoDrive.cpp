// TODO: Verify import is correct.
#include "SumitomoDrive.h"

/*
Implementation for class SumitomoDrive
*/

// SumitomoDrive::Smartris::Smartris() : nodelet::Nodelet() {
// }


void SumitomoDrive::Smartris::onInit(){
    // nh = getNodeHandle();
    ros::NodeHandle&  private_nh = getPrivateNodeHandle();
    NODELET_DEBUG("Initializing SumitomoDrive nodelet...");
    // timer_ = nh.createTimer(ros::Duration(1.0), boost::bind(& NodeletClass::timerCb, this, _1));
    pub = private_nh.advertise<std_msgs::String>("msg_out",5);
    //TODO: Change to correct topic
    //sub = private_nh.subscribe("msg_in",5, &Hello::callback, this);
}



