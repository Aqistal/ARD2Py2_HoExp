# Credits to Kathiravan Natarajan, Stackoverflow
# This file consists of the AR Drone 2.0 camera feed receiving function.
# Someone reported this code doesn't work, further experiments required.

import cv2

cam = cv2.VideoCapture('tcp://192.168.1.1:5555')
running = True
while running:
    running, frame = cam.read()
    if running:
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == 27: 
            running = False
    else:
        print 'error reading video feed'
cam.release()
cv2.destroyAllWindows()
