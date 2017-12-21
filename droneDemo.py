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
            # Esc: Stop
            running = False
            dSeq = ardEmergency(dSeq)
        elif key == 119 or key == 87:
            # W: Move forward
            dSeq = ardForward(0.5, dSeq)
        elif key == 115 or key == 83:
            # S: Move backward
            dSeq = ardBackward(0.5, dSeq)
        elif key == 97 or key == 65:
            # A: Move left
            dSeq = ardLeft(0.5, dSeq)
        elif key == 100 or key == 68:
            # D: Move right
            dSeq = ardRight(0.5, dSeq)
        elif key == 113 or key == 81:
            # Q: Rotate left
            dSeq = ardLrotate(0.5, dSeq)
        elif key == 101 or key == 69:
            # E: Rotate right
            dSeq = ardRrotate(0.5, dSeq)
        elif key == 32:
            # Space: Take off
            dSeq = ardTakeoff(dSeq)
        elif key == 13:
            # Enter: Landing
            dSeq = ardLanding(dSeq)
        elif key == 111 or key == 79:
            # O: Go up
            dSeq = ardUp(0.5, dSeq)
        elif key == 108 or key == 76:
            # L: Go down
            dSeq = ardDown(0.5, dSeq)
        else:
            # Hover when do nothing
            dSeq = ardHover(dSeq)
    else:
        print 'Error reading video feed'

cam.release()
cv2.destroyAllWindows()
