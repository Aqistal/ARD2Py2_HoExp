# Demo file 2
# Threading experiments
# Keep alive function is still unused

import cv2
import threading
from droneControl import *

cam = cv2.VideoCapture('tcp://192.168.1.1:5555')
running = True
key = 0
dSeq = 1

def keepAlive():
    global running
    while running:
        dSeq = resetWatchdog(dSeq)

def camVideo():
    global cam
    global running
    global key
    while running:
        running, frame = cam.read()
        cv2.imshow('frame', frame)
        key = cv2.waitKey(1)
        if key == 27:
            # Esc: Stop
            running = False
    cam.release()
    cv2.destroyAllWindows()

def controlLoop():
    global dSeq
    global cam
    global running
    global key
    while running:
        # Esc: Stop
        if key == 27:
            # X: Emergency stop
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
            # Do nothing: Send hovering command
            dSeq = ardHover(dSeq)
    dSeq = ardDisconnect(dSeq)

# t0 = threading.Thread(target=keepAlive)
t1 = threading.Thread(target=camVideo)
t2 = threading.Thread(target=controlLoop)
# t0.start()
t1.start()
t2.start()
