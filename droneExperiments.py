# AR Drone 2.0 test file

from droneControl import *

def droneTakeLand(cmdSeq, timeCount):
    time1 = timeCount
    time2 = timeCount / 2
    time3 = timeCount
    tx = timeCount
    cmdSeq = ardTakeoff(cmdSeq)
    while(time1):
        time1 = time1 - 1
    while(time2):
        cmdSeq = ardHover(cmdSeq)
        time2 = time2 - 1
    while(tx):
        tx = tx - 1
    cmdSeq = ardLanding(cmdSeq)
    while(time3):
        time3 = time3 - 1
    return cmdSeq

seq = droneTakeLand(3,2000)
