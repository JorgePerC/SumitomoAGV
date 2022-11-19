#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Pose2D, Twist
from std_msgs.msg import Float32,Bool,String, Int32
from canopen_chain_node.srv import SetObject


def cmd_Callback(msg):
	global motor_cmd
	motor_cmd = msg.linear.y


# init node
rospy.init_node("app")
rate = rospy.Rate(60)
#service and suscriber
rospy.wait_for_service("driver/set_object")
set_object = rospy.ServiceProxy("driver/set_object", SetObject)
rospy.Subscriber("/cmd_vel",Twist,cmd_Callback)
# variables
motor_cmd = int()



def main():
	######### SMARTRIS #######################
	node = "motorRight"
	obj = '60FF'
	k = 100
	#########################################
	try:
		#get cmd_vel.linear.y value and use service to move motor
		vel_service_call = set_object(node,obj, str(motor_cmd), False)
		print("motor in motion", motor_cmd)
		
	except rospy.ServiceException as e:
		# catch any errors
		print("Service call failed: %s"%e)
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

