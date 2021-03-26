import keyboardControlTelloModule as km
from djitellopy import Tello
import time
import cv2


_width = 690
_height = 420
km.init()
drone = Tello()
drone.connect()
print(drone.get_battery())
global img
drone.streamoff()
drone.streamon()

def getKeyInput():
    leftRight, foreBack, upNDown, yawVel = 0, 0, 0, 0
    speed = 50

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

    #Camera and Video
    elif km.getKey("g"):
        cv2.imwrite(f"Drone/Images/{time.time()}.jpg", img) 
        time.sleep(0.3)

    return [leftRight, foreBack, upNDown, yawVel]

while True:
    val = getKeyInput()
    drone.send_rc_control(val[0], val[1], val[2], val[3])

    img = drone.get_frame_read().frame
    img = cv2.resize(img, (_width, _height))
    cv2.imshow("Drone Footage", img)
    cv2.waitKey(1)



