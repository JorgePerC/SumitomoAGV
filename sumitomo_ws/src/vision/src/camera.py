#!/usr/bin/env python
import cv2
import rospy
from sensor_msgs.msg import Image
import cv_bridge

class Camera_raw:

	def __init__(self):
		rospy.init_node("camera")
		self.img_pub = rospy.Publisher("/video_source/raw",Image,queue_size=1)
		self.rate = rospy.Rate(60)
		self.frame = cv2.VideoCapture(0)
		self.frame.set(5,30)
		self.bridge = cv_bridge.CvBridge()

	def img_publish(self):
		rtr,frame = self.frame.read()
		self.img_pub.publish(self.bridge.cv2_to_imgmsg(frame,'bgr8'))

	def main(self):
		# main execution while node runs
		print("Running main...")
		while not rospy.is_shutdown():
			try:
				self.img_publish()
			except Exception as e:
				print("wait")
				print(e)
			self.rate.sleep()
		cv2.destroyAllWindows()
if __name__ == "__main__":
	try:
		node = Camera_raw()
		node.main()
	except (rospy.ROSInterruptException, rospy.ROSException("Topic interrupted")):
		pass
