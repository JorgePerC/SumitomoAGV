#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Pose2D, Twist
from std_msgs.msg import Float32,Bool,String, Int32
from canopen_chain_node.srv import SetObject

class AppSmartris:
	def __init__(self, nodeName):
		#service and suscriber
		rospy.wait_for_service("driver/set_object")
		set_object = rospy.ServiceProxy("driver/set_object", SetObject)
		rospy.Subscriber("/cmd_vel", Twist, self.cmd_Callback)

		# variables
		self.motor_cmd = 0 
		
		# init node
		rospy.init_node(nodeName)
		rate = rospy.Rate(60)

	def cmd_Callback(self, msg):
		self.motor_cmd = msg.linear.y


	def setVelocity(self):
		######### SMARTRIS #######################
		node = "motorRight"
		obj = '60FF'
		k = 100
		#########################################
		try:
			#get cmd_vel.linear.y value and use service to move motor
			vel_service_call = set_object(node, obj, str(self.motor_cmd), False)
			print("motor in motion", self.motor_cmd)
			
		except rospy.ServiceException as e:
			# catch any errors
			print("Service call failed: %s"%e)


#------------------------Main-------------------------------
if __name__ == "__main__":
	name = "app"
	node_app = AppSmartris(name)

	print("Running main ...")
	
	# while node active
	try:
		rospy.spin()
	except rospy.ROSInterruptException:
		print("Killed node", name)





