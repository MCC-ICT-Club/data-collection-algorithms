# Author: Mario Solis
# Description: This is a simple program using OpenCV
# to setup a live camera feed

import cv2 as cv


######################################################################

camNum = 0
delay = 1
quiteKey = 'q'

#######################################################################

cap = cv.VideoCapture(camNum)

while True:
    success, img = cap.read()
    img = cv.resize(img,(120, 100))

    cv.imshow("pyCam", img)

    if cv.waitKey(delay) & 0xFF == ord(quiteKey):
        break

cap.release()
cv.destroyAllWindows()

# Closing Reflection
# When creating this program I had to do a bit of referencing back to the
# code within dataCollect.py from the tutorial video I picked up for creating
# haar cascades to detect specific objects. In the process learning about
# how the cv.waitkey() function was a blocking function and its parameter
# is for specifying a delay time. The biggest thing I came to learn beyond
# having to setup a while loop to pass in live feed was how this function
# required a mask with 0xFF before setting it equal to a specific key
# as the quite program key.
# Its almost as 0xFF is turning of its blocking function property. I'm
# curious to learn more about how masking works within python and around
# OpenCV.