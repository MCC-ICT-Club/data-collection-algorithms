# Author: Mario Solis
# Description: In this program I go a step further with the
# live feed I created in the previous program. Here I begin
# to experiment with the contrast setting of the live feed.

import cv2 as cv

######################################################################

defaultBrightness = 100
defaultExposure = 50
defaultTemp = 23
defaultSharpness = 50

default = 0
count = 0
maxBrightness = 125
minBrightness = -125
camNum = 1
growthRate = 1
increment = 1
decrement = -1
delay = 1
quiteKey = 'q'

#######################################################################

cap = cv.VideoCapture(camNum)

cap.set(cv.CAP_PROP_CONTRAST, default)
cap.set(cv.CAP_PROP_BRIGHTNESS, defaultBrightness)
cap.set(cv.CAP_PROP_EXPOSURE, defaultExposure)
cap.set(cv.CAP_PROP_TEMPERATURE, defaultTemp)
cap.set(cv.CAP_PROP_SHARPNESS, defaultSharpness)

while True:
    success, img = cap.read()

    cv.imshow("pyCamContrast", img)

    if cv.waitKey(delay) & 0xFF == ord(quiteKey):
        break

    cap.set(cv.CAP_PROP_CONTRAST, count)

    count += growthRate
    print(count)

    if count == minBrightness:
        growthRate = increment

    if count == maxBrightness:
        growthRate = decrement


cap.release()
cv.destroyAllWindows()


# Closing Reflection
# It appears as though with the contrast property. Once you raise it up a certain level. It does not come
# back down.

# An idea worth trying would be to once the contrast has been raised up to a certain point. Then decrement the
# exposure of the cam to see if then the contrast can be readjusted with the changed exposure setting.

# Update: after setting the default setting for set of other camera properties I've succesfully gotten the
# contrast to oscilate between the minimum and maximum