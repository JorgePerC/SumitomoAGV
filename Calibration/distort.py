import cv2
import numpy as np
cam = cv2.VideoCapture(0)

rest,frame = cam.read()
# -- correct barrel distortion from camera --
width = frame.shape[1]
height = frame.shape[0]
# vector of coeffs
distCoeff = np.zeros((4,1),np.float64)
# callibration
k1 = -1.0e-6;	# negative to remove barrel distortion
k2 = -1.0e-11;
p1 = 3.0e-6;
p2 = 2.0e-4;
distCoeff[0,0] = k1;
distCoeff[1,0] = k2;
distCoeff[2,0] = p1;
distCoeff[3,0] = p2;
# assume unit matrix for camera
cam = np.eye(3,dtype=np.float32)
cam[0,2] = width/2.0 # define center x
cam[1,2] = height/2.0 # define center y
cam[0,0] = 4  # define focal length x
cam[1,1] = 4  # define focal length y
# undistortion
dst = cv2.undistort(frame,cam,distCoeff) # frame, 
#camMatrix, vector of undistortion coefs

		# copy for writing final output on it
cv2.imshow("cam1",dst)
cv2.waitKey(0)
