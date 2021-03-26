import keyboardControlTelloModule as km
from djitellopy import Tello
from time import sleep


# ###NOTE####
# This program dosent have real-time recording shown from the tello.
# However, it's very easy to add! You can try adding video feed,
# then you can check your work with "cameraKeyboardControlTello.py"
# also in my repository.
# ###########


km.init()
drone = Tello()
drone.connect()
print(drone.get_battery())

def getKeyInput():
    leftRight, foreBack, upNDown, yawVel = 0, 0, 0, 0
    speed = 60

    #Controls with WASD;
    if km.getKey("w"): foreBack = speed #Foreward
    elif km.getKey("s"): foreBack = -speed #Back
    elif km.getKey("a"): leftRight = -speed #Left
    elif km.getKey("d"): leftRight = speed #Right
    elif km.getKey("h"): upNDown = speed #Makes the drone go up
    elif km.getKey("j"): upNDown = -speed #Makes the drone go down
    elif km.getKey("y"): yawVel = -speed #Turns the drone counterclockwise
    elif km.getKey("u"): yawVel = speed #Turns the drone clockwise
    
    #Landing and Takeoff
    elif km.getKey("ESCAPE"): drone.emergency() #EMERGENCY LANDING; if land command isnt going through
    elif km.getKey("SPACE"): drone.takeoff() #Takeoff the drone
    elif km.getKey("RETURN"): drone.land() #Enter Key

    return [leftRight, foreBack, upNDown, yawVel]

while True:
    val = getKeyInput()
    drone.send_rc_control(val[0], val[1], val[2], val[3])
    sleep(0.069)
