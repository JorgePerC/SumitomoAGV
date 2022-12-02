#!/usr/bin/env python
import rospy
import numpy as np
from geometry_msgs.msg import Pose2D, Twist
from std_msgs.msg import Float32, Bool, String

class LineFollower:
	def __init__(self):
		self.cam_x = 0
		self.cam_y = 0
		self.box_theta = 0
		self.box_y = 0
		self.box_x = 0				

		# publisher and subscribers and variables
		self.cmd_pub = rospy.Publisher("/cmd_vel", Twist, queue_size = 1)
		rospy.Subscriber("/cam_center", Pose2D, self.camCallback)
		rospy.Subscriber("/box_center", Pose2D, self.boxCallback)
		
		# init node
		rospy.init_node("controller")
		self.rate = rospy.Rate(30)
		
		

	# callbacks
	def end_Callback(self):
		# stop at last
		new_cmd = Twist()
		new_cmd.linear.x = 0.0
		new_cmd.linear.y = 0.0
		new_cmd.angular.z = 0.0
		self.cmd_pub.publish(new_cmd)

	def camCallback(self, msg):
		# camera center
		self.cam_x = msg.x
		self.cam_y = msg.y

	def boxCallback(self, msg):
		# box center
		self.box_x = msg.x
		self.box_y = msg.y
		self.box_theta = msg.theta


	# functions for robot movement
	''' falta hacer prubas para determinar el valor de la proporcional k'''
	def follow(self, maxvel=100000, K=0.09):
		new_cmd = Twist()
		while not rospy.is_shutdown():
			# following line based on box and camera centers
			print("following line......")
			# proportional gain for control of the difference centers coordinates
			x_dif = (self.box_x - self.cam_x) * -K
			y_dif = (self.box_y - self.cam_y) * -K
			# incoming turn -> slow linear velocity
			if (self.box_theta < -75 and self.box_theta > -80) or (self.box_theta < -15 and self.box_theta > -20):
				new_cmd.linear.y = maxvel/2
			else:
				new_cmd.linear.y = maxvel
			# angular speed saturation
			''' *falta definir la saturacion de velocidad angular ( de ser necesario)
			    * falta determinar la velocidad angular para las vueltas
			if x_dif < -0.2:
				new_cmd.angular.z = -0.2
			elif x_dif > 0.2:
				new_cmd.angular.z = 0.2
			# move towards the center of line detected -> adjust angular vel
			else:
				new_cmd.angular.z = x_dif 
			'''
			# publish velocity
			self.cmd_pub.publish(new_cmd)

#------------------------Main-------------------------------
print("Running main ...")

follower = LineFollower()
try:
	follower.follow()
	rospy.spin()
except rospy.ROSInterruptException:
	rospy.on_shutdown(follower.end_Callback)
	print("ROS Interrupt Exception, done by user")
except rospy.ROSTimeMovedBackwardsException:
	rospy.logerr("ROS Time Backwards! just ignore")
	
print("exited")
