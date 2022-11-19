#!/usr/bin/env python
import rospy
import numpy as np
from geometry_msgs.msg import Pose2D, Twist
from std_msgs.msg import Float32,Bool,String, Int32
from canopen_chain_node.srv import SetObject
from std_srvs.srv import Trigger


def cmdCallback(msg):
	global cmdx
	global cmdy
	cmdx = msg.linear.x
	cmdy = msg.linear.y

def end_Callback():
	# stop at last
	vel_service_call = set_object('motorRight','0x60FF', '0', False)

rospy.Subscriber("/cmd_vel",Twist,cmdCallback)
motor_md = Twist()

def SmartrisRun(vel):
	######### SMARTRS #######################
	node = "motorRight"
	obj = '0x60FF'
	k = 10
	#########################################
	vel_service_call = set_object(node,obj, str(cmdy * k), False)
	print("motor in motion")

def main():
	rospy.wait_for_service("driver/set_object")
	SmartrisRun()
#------------------------Main-------------------------------
print("Running main ...")
while not rospy.is_shutdown():
	# while node active
	try:
		main()
	except rospy.ROSInterruptException:
		rospy.on_shutdown(end_Callback)
		print("ROS Interrupt Exception, done by user")
	except rospy.ROSTimeMovedBackwardsException:
		rospyu.logerr("ROS Time Backwards! just ignore")
	rate.sleep()
end_Callback()
