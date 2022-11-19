#!/usr/bin/env python
import rospy
import numpy as np
from geometry_msgs.msg import Pose2D, Twist
from std_msgs.msg import Float32,Bool,String, Int32
from canopen_chain_node.srv import SetObject
from std_srvs.srv import Trigger

# callbacks
def end_Callback():
	# stop at last
	robot_cmd.linear.x = 0.0
	robot_cmd.angular.z = 0.0
	

def camCallback(msg):
	# camera center
	global cam_x
	global cam_y
	cam_x = msg.x
	cam_y = msg.y

def boxCallback(msg):
	# box center
	global box_x
	global box_y
	global box_theta
	box_x = msg.x
	box_y = msg.y
	box_theta = msg.theta

def zebraCallback(msg):
	# crosswalk
	global zebra
	zebra = msg.data

def onesCallback(msg):
	# lines
	global line
	line = msg.data

def zeroCallback(msg):
	# zero contours
	global zero
	zero = msg.data

def classCallback(msg):
	# sign class
	global label
	label = msg.data

def probCallback(msg):
	# sign class probability
	global prob
	prob = msg.data

def lightCallback(msg):
	# light color
	global light
	light = msg.data
def VelCallback(msg):
	global velant
	velant = msg.data


# init node
rospy.init_node("controller")
# publisher and subscribers and variables

############# SMARTRS ##############
rospy.wait_for_service("driver/set_object")
set_object = rospy.ServiceProxy("driver/set_object", SetObject)
rospy.wait_for_service("driver/init")
driverInit = rospy.ServiceProxy("driver/init", Trigger)
init_call = driverInit()
rospy.Subscriber("/motorRight_60FF",Int32,VelCallback)
###################################3
rospy.Subscriber("/cam_center",Pose2D,camCallback)
rospy.Subscriber("/box_center",Pose2D,boxCallback)
rospy.Subscriber("/zebra",Bool,zebraCallback)
rospy.Subscriber("/line",Bool,onesCallback)
rospy.Subscriber("/zero",Bool,zeroCallback)
rospy.Subscriber("/classify/class",String,classCallback)
rospy.Subscriber("/light",String,lightCallback)
rospy.Subscriber("/classify/prob",Float32,probCallback)
rate = rospy.Rate(60)
robot_cmd = Twist()
cam_x = float()
cam_y = float()
box_x = float()
box_y = float()
box_theta = float()
light = ""
zebra = False
line = False
zero = False
label = ""
prob = float()
in_crosswalk = False
continue_line = False
wait_green = False
in_process = ""
maxvelSmar = 100000
velant = 0

# functions for robot movement
def stop():
	# stop robot
	print("stoping...")
	robot_cmd.linear.x = 0.0
	robot_cmd.angular.z = 0.0
	

def cross_straight(maxvel = 100):
	# passing crosswalk straight
	print("crosswalk straight...")
	robot_cmd.angular.z = 0
	robot_cmd.linear.x = maxvel
	

def cross_right(maxvel=100,R=2):
	# passing crosswalk turning right
	print("crosswalk right...")
	robot_cmd.linear.x = maxvel
	robot_cmd.angular.z = -0.045	# (1/R)*maxvel -> ideal circular turn

def SmartrisRun(vel):
	######### SMARTRS #######################
	node = "motorRight"
	obj = '0x60FF'
	#########################################
	vel_service_call = set_object(node,obj, str(vel), False)
	print("motor in motion")
		
	



def follow(maxvel=100, K=0.09):
	# following line based on box and camera centers
	print("following line...")
	# proportional gain for control of the difference centers coordinates
	x_dif = (box_x - cam_x) * -K
	y_dif = (box_y - cam_y) * -K
	# incoming turn -> slow linear velocity
	if (box_theta < -75 and box_theta > -80) or (box_theta < -15 and box_theta > -20):
		robot_cmd.linear.x = maxvel/2
################################### SMARTRIS ########################
		vel = maxvelSmar/2
####################################################################
	else:
		robot_cmd.linear.x = maxvelSmar
############################ SMARTRIS ################################
		vel = maxvelSmar
######################################################################
	# angular speed saturation
	if x_dif < -0.4:
		robot_cmd.angular.z = -0.2
############################ SMARTRIS ################################
		vel = maxvelSmar * -1
######################################################################
	elif x_dif > 0.4:
		robot_cmd.angular.z = 0.2
############################ SMARTRIS ################################
		vel = maxvelSmar
######################################################################
	# move towards the center of line detected -> adjust angular vel
	else:
		robot_cmd.angular.z = x_dif
############################ SMARTRIS ################################
		vel = x_dif * maxvelSmar
		vel = vel
		
######################################################################
	SmartrisRun(vel)

def main():
	rospy.wait_for_service("driver/set_object")
	follow()
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
