# Python file for AR Drone 2.0 controlling
# No camera included
# Please use with care

import socket
import struct

droneIP = "192.168.1.1"
dronePort = 5556
droneSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def ardTakeoff(cmdSeq):
    print "Drone takingoff"
    droneComd = "AT*FTRIM=%i,\r" % (cmdSeq)
    droneSock.sendto(droneComd, (droneIP, dronePort))
    cmdSeq = cmdSeq + 1
    droneComd = "AT*CONFIG=%i,%s\r" % (cmdSeq,"\"control:altitude_max\", \"20000\"")
    droneSock.sendto(droneComd, (droneIP, dronePort))
    cmdSeq = cmdSeq + 1
    droneComd = "AT*REF=%i,%s\r" % (cmdSeq,"290718208")
    droneSock.sendto(droneComd, (droneIP, dronePort))
    cmdSeq = cmdSeq + 1
    return cmdSeq

def ardLanding(cmdSeq):
    print "Drone landing"
    droneComd = "AT*REF=%i,%s\r" % (cmdSeq,"290717696")
    droneSock.sendto(droneComd, (droneIP, dronePort))
    cmdSeq = cmdSeq + 1
    return cmdSeq

def ardEmergency(cmdSeq):
    print "EMERGENCY DRONE SHUT DOWN IN PROGRESS"
    droneComd = "AT*REF=%i,%s\r" % (cmdSeq,"290717952")
    droneSock.sendto(droneComd, (droneIP, dronePort))
    cmdSeq = cmdSeq + 1
    droneComd = "AT*REF=%i,%s\r" % (cmdSeq,"290717696")
    droneSock.sendto(droneComd, (droneIP, dronePort))
    cmdSeq = cmdSeq + 1
    return cmdSeq

def ardHover(cmdSeq):
    print "Hovering"
    droneComd = "AT*PCMD=%i,%s\r" % (cmdSeq,"1,0,0,0,0")
    droneSock.sendto(droneComd, (droneIP, dronePort))
    cmdSeq = cmdSeq + 1
    return cmdSeq

def ardForward(speed, cmdSeq):
    print "Moving forward"
    if type(speed) == float:
        spd = struct.unpack('i', struct.pack('f', speed))[0]
    else:
        spd = speed
    droneComd = "AT*PCMD=%i,%i,%i,%i,%i,%i\r" % (cmdSeq,1,-spd,0,0,0)
    droneSock.sendto(droneComd, (droneIP, dronePort))
    cmdSeq = cmdSeq + 1
    return cmdSeq

def ardBackward(speed, cmdSeq):
    print "Moving backward"
    if type(speed) == float:
        spd = struct.unpack('i', struct.pack('f', speed))[0]
    else:
        spd = speed
    droneComd = "AT*PCMD=%i,%i,%i,%i,%i,%i\r" % (cmdSeq,1,spd,0,0,0)
    droneSock.sendto(droneComd, (droneIP, dronePort))
    cmdSeq = cmdSeq + 1
    return cmdSeq

def ardLeft(speed, cmdSeq):
    print "Moving left"
    if type(speed) == float:
        spd = struct.unpack('i', struct.pack('f', speed))[0]
    else:
        spd = speed
    droneComd = "AT*PCMD=%i,%i,%i,%i,%i,%i\r" % (cmdSeq,1,0,-spd,0,0)
    droneSock.sendto(droneComd, (droneIP, dronePort))
    cmdSeq = cmdSeq + 1
    return cmdSeq

def ardRight(speed, cmdSeq):
    print "Moving right"
    if type(speed) == float:
        spd = struct.unpack('i', struct.pack('f', speed))[0]
    else:
        spd = speed
    droneComd = "AT*PCMD=%i,%i,%i,%i,%i,%i\r" % (cmdSeq,1,0,spd,0,0)
    droneSock.sendto(droneComd, (droneIP, dronePort))
    cmdSeq = cmdSeq + 1
    return cmdSeq

def ardUp(speed, cmdSeq):
    print "Moving up"
    if type(speed) == float:
        spd = struct.unpack('i', struct.pack('f', speed))[0]
    else:
        spd = speed
    droneComd = "AT*PCMD=%i,%i,%i,%i,%i,%i\r" % (cmdSeq,1,0,0,spd,0)
    droneSock.sendto(droneComd, (droneIP, dronePort))
    cmdSeq = cmdSeq + 1
    return cmdSeq

def ardDown(speed, cmdSeq):
    print "Moving down"
    if type(speed) == float:
        spd = struct.unpack('i', struct.pack('f', speed))[0]
    else:
        spd = speed
    droneComd = "AT*PCMD=%i,%i,%i,%i,%i,%i\r" % (cmdSeq,1,0,0,-spd,0)
    droneSock.sendto(droneComd, (droneIP, dronePort))
    cmdSeq = cmdSeq + 1
    return cmdSeq

def ardLrotate(omega, cmdSeq):
    print "Rotate left"
    if type(omega) == float:
        spd = struct.unpack('i', struct.pack('f', omega))[0]
    else:
        spd = speed
    droneComd = "AT*PCMD=%i,%i,%i,%i,%i,%i\r" % (cmdSeq,1,0,0,0,-spd)
    droneSock.sendto(droneComd, (droneIP, dronePort))
    cmdSeq = cmdSeq + 1
    return cmdSeq

def ardRrotate(omega, cmdSeq):
    print "Rotate right"
    if type(speed) == float:
        spd = struct.unpack('i', struct.pack('f', omega))[0]
    else:
        spd = speed
    droneComd = "AT*PCMD=%i,%i,%i,%i,%i,%i\r" % (cmdSeq,1,0,0,0,spd)
    droneSock.sendto(droneComd, (droneIP, dronePort))
    cmdSeq = cmdSeq + 1
    return cmdSeq
