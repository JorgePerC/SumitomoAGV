#!/usr/bin/env python
import rospy
from canopen_chain_node.srv import SetObject
from std_srvs.srv import Trigger

def initSmartris(node,obj, val):
	#Code that generates the sequence to get the Smartris to run state
	#rosservice that changes objects form the eds
	set_object = rospy.ServiceProxy("driver/set_object", SetObject, persistent=True) #  , persistent=True
	try:
		
		# call the rosservice with your node name, object and the value you want
		# last value is a boolean for the cached part of the setObject msg
		service_call = set_object(node,obj, val, True)
		print("Servie response is:" , service_call)
	except rospy.ServiceException as e:
		# catch any errors
		print("Service call failed: %s"%e)


if __name__ == "__main__":
	#wait for the services to initalize 
	rospy.wait_for_service("driver/set_object")
	rospy.wait_for_service("driver/init")
	# put the Smartris in Init mode 
	driverInit = rospy.ServiceProxy("driver/init", Trigger)
        init_call = driverInit()
	rospy.sleep(.3)
	#initialize your parameters
	node = "motorRight"
	# create two list with the object and the msg in order to create
	# the sequence
	objects = ['0x6060', '0x6040','0x6040','0x6040']
	values =['0x040B', '0x06', '0x07', '0x0F']
	# run the sequence 
	for i in xrange(len(values)):
		initSmartris(node, objects[i],values[i])
		# wait to make sure all messages have time to be sent 
		# other values may work
		rospy.sleep(.3)

	print("Smartris in run")
	
	
		
		
		
		
