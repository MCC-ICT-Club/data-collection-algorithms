# Author: Mario Solis
# Description: In this program I go a step further with the
# live feed I created in the previous program. Here I begin
# to experiment with the sharpness setting of the live feed.


import cv2 as cv

######################################################################

defaultBrightness = 100
defaultExposure = 50
defaultTemp = 23
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

cap.set(cv.CAP_PROP_SHARPNESS, minBrightness)
cap.set(cv.CAP_PROP_BRIGHTNESS, defaultBrightness)
cap.set(cv.CAP_PROP_EXPOSURE, defaultExposure)
cap.set(cv.CAP_PROP_TEMPERATURE, defaultTemp)

while True:
    success, img = cap.read()

    cv.imshow("pyCamSharpness", img)

    if cv.waitKey(delay) & 0xFF == ord(quiteKey):
        break

    cap.set(cv.CAP_PROP_SHARPNESS, count)

    count += growthRate
    print(count)

    if count == minBrightness:
        growthRate = increment

    if count == maxBrightness:
        growthRate = decrement


cap.release()
cv.destroyAllWindows()

# Closing Reflection
# This one seems to have the crispiest image out of all even though theres no majorly noticable change occuring
# on the image as it ocsillates

# Then again the more I look at it the more I feel like there is a change occuring I just dont have the proper
# test subject to clearly show it.