import cv2
print ("OpenCV imported")

def gstreamer_pipeline(
    capture_width=1024,
    capture_height=1280,
    display_width=512,
    display_height=640,
    framerate=30,
    flip_method=0, ):
    return (
        "nvarguscamerasrc ! "
        "video/x-raw(memory:NVMM), "
        "width=(int)%d, height=(int)%d, "
        "format=(string)NV12, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink"
        % (
            capture_width,
            capture_height,
            framerate,
            flip_method,
            display_width,
            display_height,
        )
    )


#capture = cv2.VideoCapture(gstreamer_pipeline(flip_method=0), cv2.CAP_GSTREAMER)
        #framerate=10, display_width = 640, display_height =  480

capture = cv2.VideoCapture(1)
while True:
    succ, img = capture.read()
    cv2.imshow("CSI Camera", img)
    keyCode = cv2.waitKey(30) & 0xFF
    # Stop the program on the ESC key
    if keyCode == 27:
        break
cv2.destroyAllWindows()
