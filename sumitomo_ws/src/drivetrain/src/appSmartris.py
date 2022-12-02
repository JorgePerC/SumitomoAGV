#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Pose2D, Twist
from std_msgs.msg import Float32,Bool,String, Int32
from canopen_chain_node.srv import SetObject

class AppSmartris:
	def __init__(self, nodeName):
		#service and suscriber
		rospy.wait_for_service("driver/set_object")
		self.set_object = rospy.ServiceProxy("driver/set_object", SetObject)
		rospy.Subscriber("/cmd_vel", Twist, self.cmd_Callback)
		rospy.Subscriber("/Ultra", Float32, self.ultra_fault)

		# variables
		self.motor_cmd = 0 
		
		# init node
		rospy.init_node(nodeName)
		rate = rospy.Rate(60)

	def cmd_Callback(self, msg):
		self.motor_cmd = msg.linear.y
		
	def ultra_fault(self, msg):
		dist = msg.data
		
		if dist < 40: # These are cm
			self.motor_cmd = 0
		

	def setVelocity(self):
		######### SMARTRIS #######################
		node = "motorRight"
		obj = '60FF'
		k = 100
		#########################################
		try:
			#get cmd_vel.linear.y value and use service to move motor

			# Check if the ultrasonic is being blocked
			
			vel_service_call = self.set_object(node, obj, str(self.motor_cmd * 10), False)
			print("motor in motion", self.motor_cmd)
			
		except rospy.ServiceException as e:
			# catch any errors
			print("Service call failed: %s"%e)


#------------------------Main-------------------------------
if __name__ == "__main__":
	name = "app"
	node_app = AppSmartris(name)

	print("Running main ...")
	while not rospy.is_shutdown():
	# while node active
		try:
			node_app.setVelocity()
		except rospy.ROSInterruptException:
			print("Killed node", name)





