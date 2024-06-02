# Author: Mario Solis
# Description: In this program I go a step further with the
# live feed I created in the previous program. Here I begin
# to experiment with the monochrome setting of the live feed.


import cv2 as cv

######################################################################

default = 0
count = 0
maxBrightness = 365
minBrightness = 0
camNum = 1
growthRate = 1
increment = 1
decrement = -1
delay = 1
quiteKey = 'q'

#######################################################################

cap = cv.VideoCapture(camNum)

cap.set(cv.CAP_PROP_MONOCHROME, default)

while True:
    success, img = cap.read()

    cv.imshow("pyCamMonochrome", img)

    if cv.waitKey(delay) & 0xFF == ord(quiteKey):
        break

    cap.set(cv.CAP_PROP_MONOCHROME, count)

    count += growthRate

    if count == minBrightness:
        growthRate = increment

    if count == maxBrightness:
        growthRate = decrement


cap.release()
cv.destroyAllWindows()