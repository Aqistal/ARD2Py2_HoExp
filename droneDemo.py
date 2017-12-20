# Demo file
# Move drone using keyboard and the camera

import cv2
from droneControl import *

cam = cv2.VideoCapture('tcp://192.168.1.1:5555')

running = True
dSeq = 1

while running:
    running, frame = cam.read()
    if running:
        cv2.imshow('frame', frame)
        key = cv2.waitKey(1)
        if key == 27:
            running = False
            dSeq = ardEmergency(dSeq)
        else if key == 119 or key == 87:
            # Move forward
            dSeq = ardForward(0.5, dSeq)
        else if key == 115 or key == 83:
            # Move backward
            dSeq = ardBackward(0.5, dSeq)
        else if key == 97 or key == 65:
            # Move left
            dSeq = ardLeft(0.5, dSeq)
        else if key == 100 or key == 68:
            # Move right
            dSeq = ardRight(0.5, dSeq)
        else if key == 113 or key == 81:
            # Rotate left
            dSeq = ardLrotate(0.5, dSeq)
        else if key == 101 or key == 69:
            # Rotate right
            dSeq = ardRrotate(0.5, dSeq)
        else if key == 32:
            # Take off
            dSeq = ardTakeoff(dSeq)
        else if key == 13:
            # Landing
            dSeq = ardLanding(dSeq)
        else if key == 111 or key == 79:
            # Go up
            dSeq = ardUp(0.5, dSeq)
        else if key == 108 or key == 76:
            # Go down
            dSeq = ardDown(0.5, dSeq)
        else:
            # Do nothing
    else:
        print 'Error reading video feed'

cam.release()
cv2.destroyAllWindows()
