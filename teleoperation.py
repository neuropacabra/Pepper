from robot import Pepper
import cv2

pepper = Pepper("10.37.1.227")
pepper.set_security_distance(0.01)

image = cv2.imread("src/keyboard.png")
height, width = image.shape[:2]

cv2.namedWindow("Robot teleoperation", cv2.WINDOW_GUI_NORMAL)
cv2.resizeWindow("Robot teleoperation", width, height)

while True:
    cv2.imshow("Robot teleoperation", image)
    k = cv2.waitKeyEx()
    if k == 27:
        break

    if k == 100:
        # Turn right
        pepper.turn_around(-2)
    elif k == 119:
        # Go forward
        pepper.move_forward(2)
    elif k == 97:
        # Turn left
        pepper.turn_around(2.0)
    elif k == 115:
        # Go back
        pepper.move_forward(2.0)
    elif k == 32:
        # Stop moving
        pepper.stop_moving()
