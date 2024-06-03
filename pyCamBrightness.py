# Author: Mario Solis
# Description: In this program I go a step further with the
# live feed I created in the previous program. Here I begin
# to experiment with the brightness setting of the live feed.

import cv2 as cv

######################################################################

default = 0
count = 0
maxBrightness = 265
minBrightness = 0
camNum = 1
growthRate = 1
increment = 1
decrement = -1
delay = 1
quiteKey = 'q'

#######################################################################

cap = cv.VideoCapture(camNum)

cap.set(cv.CAP_PROP_BRIGHTNESS, default)

while True:
    success, img = cap.read()

    cv.imshow("pyCamBrightness", img)

    if cv.waitKey(delay) & 0xFF == ord(quiteKey):
        break

    cap.set(cv.CAP_PROP_BRIGHTNESS, count)

    count += growthRate
    print(count)

    if count == minBrightness:
        growthRate = increment

    if count == maxBrightness:
        growthRate = decrement


cap.release()
cv.destroyAllWindows()

# Closing Reflection
# When creating this program I familiarized myself with the properties of
# cv.CAP_PROP_BRIGHTNESS and by trial and error I cam to determine its
# maximum and minimum values as 365 and 0 when observing the changes occuring
# on the live feed.

