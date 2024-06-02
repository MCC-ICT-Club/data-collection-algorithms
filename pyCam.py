# Author: Mario Solis
# Description: This is a simple program using OpenCV
# to setup a live camera feed

import cv2 as cv

cap = cv.VideoCapture(1)

while True:
    success, img = cap.read()

    cv.imshow("pyCam", img)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
