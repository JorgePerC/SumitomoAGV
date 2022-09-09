// TODO: Verify import is correct.
#include "SumitomoDrive.h"

/*
Implementation for class SumitomoDrive
*/



SumitomoDrive::Smartris::Smartris(){

}

void SumitomoDrive::Smartris::OnInit(){
    nh = getNodeHandle();
    private_nh = getPrivateNodeHandle();
    // timer_ = nh.createTimer(ros::Duration(1.0), boost::bind(& NodeletClass::timerCb, this, _1));
    // sub_ = nh.subscribe("incoming_chatter", 10, boost::bind(& NodeletClass::messageCb, this, _1));
    pub_ = private_nh.advertise<std_msgs::String>("outgoing_chatter", 10);
}
