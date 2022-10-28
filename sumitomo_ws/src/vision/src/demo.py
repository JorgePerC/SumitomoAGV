#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Float32

class Demo():

	def __init__(self):
		# constructor node publishers and subscribers and class variables
		
		rospy.Subscriber("/Ultra", Float32, self.ultraCallback)
		self.cmd_pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
		
		rospy.init_node("ut_demo")
		self.dist = 0.0
		self.vel = Twist()
		self.rate = rospy.Rate(60)

	def ultraCallback(self,msg):
		# callback for the distance
		self.dist = msg.data

	def processSerial(self):
		ultra = Twist()
		if self.dist > 10:
			ultra.angular.z = 0.5
		else:
			ultra.angular.z = 0
		self.cmd_pub.publish(ultra)

	def main(self):
		# main execution while node runs
		print("Running main...")
		while not rospy.is_shutdown():
			try:
				self.processSerial()
			except Exception as e:
				print("wait")
				print(e)
			self.rate.sleep()

if __name__ == "__main__":
	try:
		node = Demo()
		node.main()
	except (rospy.ROSInterruptException, rospy.ROSException("Topic interrupted")):
		pass
