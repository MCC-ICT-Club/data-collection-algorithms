# Author: Mario Solis
# Description: In this program I go a step further with the
# live feed I created in the previous program. Here I begin
# to experiment with the gain setting of the live feed.


import cv2 as cv

######################################################################

defaultBrightness = 100
defaultExposure = 50
defaultTemp = 23
defaultSharpness = 50

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

cap.set(cv.CAP_PROP_GAIN, default)
cap.set(cv.CAP_PROP_BRIGHTNESS, defaultBrightness)
cap.set(cv.CAP_PROP_EXPOSURE, defaultExposure)
cap.set(cv.CAP_PROP_TEMPERATURE, defaultTemp)
cap.set(cv.CAP_PROP_SHARPNESS, defaultSharpness)

while True:
    success, img = cap.read()

    cv.imshow("pyCamGain", img)

    if cv.waitKey(delay) & 0xFF == ord(quiteKey):
        break

    cap.set(cv.CAP_PROP_GAIN, count)

    count += growthRate

    if count == minBrightness:
        growthRate = increment

    if count == maxBrightness:
        growthRate = decrement


cap.release()
cv.destroyAllWindows()

# Closing Reflection
# This is another one where there isnt much visible change occuring with the current test subject.
# further testing will be required to view how much of an impact the changes in this property is
# having on the final image.