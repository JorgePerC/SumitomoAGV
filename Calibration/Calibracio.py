import numpy as np
import cv2
import glob

cam=cv2.VideoCapture(0)
result, image = cam.read()
if result:
    cv2.imshow('Tablero',image)
    cv2.imwrite('Tablero.jpg',image)
# termination criterio
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
 
# preparar puntos de objeto, como (0,0,0,0), (1,0,0,0), (2,0,0,0)...., (6,5,0)
objp = np.zeros((6*7,3), np.float32)
objp[:,:2] = np.mgrid[0:7,0:6].T.reshape(-1,2)
 
# Arrays para almacenar puntos de objeto y puntos de imagen de todas las imágenes.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.
 
images = glob.glob('samples/cpp/left01.jpg')
for fname in images:
  img = cv2.imread(fname)
  gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
 
  # Encuentra las esquinas del tablero de ajedrez
  ret, corners = cv2.findChessboardCorners(gray, (7,6),None)
 
  # Si se encuentran, añada puntos de objeto, puntos de imagen (después de refinarlos)
  if ret == True:
    objpoints.append(objp)
 
    corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
    imgpoints.append(corners2)
 
    # Dibuja y muestra las esquinas
    img = cv2.drawChessboardCorners(img, (7,6), corners2,ret)
    cv2.imshow('img',img)
    cv2.waitKey(500)
 
cv2.destroyAllWindows()