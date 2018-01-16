# StickEmUp
# - Simple sanity check for 3DR Solo RC inputs -
# - (c) 2018 Hampton Morgan
# - Learn more at k4kfh.github.io

#!/usr/bin/python
import dronekit
from time import sleep

connectionString = "udpout:127.0.0.1:14560"
solo = dronekit.connect(connectionString, wait_ready=True, status_printer=None)

#shortcuts for accessing channels
roll = 1
pitch = 2
throttle = 3
yaw = 4

stickWarning = False

change = {
1 : 0,
2 : 0,
3 : 0,
4 : 0,
}

previous = {
1 : solo.channels[1],
2 : solo.channels[2],
3 : solo.channels[3],
4 : solo.channels[4],
}

cycles = 0

while cycles < 100:
    #print("Throttle = " + str(solo.channels[throttle]))
    #print("Yaw = " + str(solo.channels[yaw]))
    #print("Pitch = " + str(solo.channels[pitch]))
    #print("Roll = " + str(solo.channels[roll]))
    change[roll] = change[roll] + abs(solo.channels[roll] - previous[roll])
    change[pitch] = change[pitch] + abs(solo.channels[pitch] - previous[pitch])
    change[throttle] = change[throttle] + abs(solo.channels[throttle] - previous[throttle])
    change[yaw] = change[yaw] + abs(solo.channels[throttle] - previous[throttle])
    previous = {
    1 : solo.channels[1],
    2 : solo.channels[2],
    3 : solo.channels[3],
    4 : solo.channels[4],
    }
    sleep(0.1)
    cycles = cycles + 1

print("StickEmUp.py")
print("------------")
print("Safeguard against dead RC channels")
#print("YAW CHANGE = " + str(change[yaw]))
#print("ROLL CHANGE = " + str(change[roll]))
#print("PITCH CHANGE = " + str(change[pitch]))
#print("THROTTLE CHANGE = " + str(change[throttle]))
if (change[yaw] > 1000):
    print("Yaw Change > 1000 - YAW HEALTHY!")
else:
    print("YAW STICK WARNING!")
    stickWarning = True
if (change[roll] > 1000):
    print("Roll Change > 1000 - ROLL HEALTHY!")
else:
    print("ROLL STICK WARNING!")
    stickWarning = True
if (change[pitch] > 1000):
    print("Pitch Change > 1000 - PITCH HEALTHY!")
else:
    print("PITCH STICK WARNING!")
    stickWarning = True
if (change[throttle] > 1000):
    print("Throttle Change > 1000 - THROTTLE HEALTHY!")
else:
    print("THROTTLE STICK WARNING!")
    stickWarning = True

if stickWarning:
    print("---------")
    print("DO NOT ARM VEHICLE!!!")
    print("---------")
    print("CONTROLLER MAY EXPERIENCE FATAL FAILURE!")
    print("---------")
