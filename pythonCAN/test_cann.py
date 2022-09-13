#hola
from pycanopen import *
import sys
import ctypes
canopen = CANopen()
def readCAN():
	while True:
    		canopen_frame = canopen.read_frame()
    		if canopen_frame:
        		print(canopen_frame)
    		else:
        		print("CANopen Frame parse error")
def sendCAN():
        while True:
               return canopen.send_frame(c_int(1122334455667788))
                


op =  input("Read 1 Send 2: ")
if str(op) == "1":
	while True:
		readCAN()
elif str(op) == "2":
        while True:
                sendCAN()
else:
	print("pon 1 o 2 cawn")
