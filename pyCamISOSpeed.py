# Author: Mario Solis
# Description: In this program I go a step further with the
# live feed I created in the previous program. Here I begin
# to experiment with the ISO Speed setting of the live feed.


import cv2 as cv

######################################################################

defaultBrightness = 100
defaultExposure = 50
defaultTemp = 23
defaultSharpness = 50

default = 0
count = 0
maxBrightness = 60
minBrightness = 0
camNum = 1
growthRate = 1
increment = 1
decrement = -1
delay = 100
quiteKey = 'q'

#######################################################################

cap = cv.VideoCapture(camNum)

cap.set(cv.CAP_PROP_ISO_SPEED, default)
cap.set(cv.CAP_PROP_BRIGHTNESS, defaultBrightness)
cap.set(cv.CAP_PROP_EXPOSURE, defaultExposure)
cap.set(cv.CAP_PROP_TEMPERATURE, defaultTemp)
cap.set(cv.CAP_PROP_SHARPNESS, defaultSharpness)

while True:
    success, img = cap.read()

    cv.imshow("pyCamISO_Speed", img)

    if cv.waitKey(delay) & 0xFF == ord(quiteKey):
        break

    cap.set(cv.CAP_PROP_ISO_SPEED, count)

    count += growthRate
    print(count)
    if count == minBrightness:
        growthRate = increment

    if count == maxBrightness:
        growthRate = decrement


cap.release()
cv.destroyAllWindows()

# Closing Reflection
# This is another one similar to contrast in that once its been raised up it cant be brought down.

# Another idea worth trying with these types of camera setting would be have the value jump to specific amounts
# and remain there for a time. Its possible that with the constant stream of frames coming in these particular
# settings arent currently having enough time to update.

# Another area worth tinkering with to test out how these changes are taking effect would be in looking at
# different delay values and how they impact the changes in camera setting.
# Update: even with the changed delay time the ISO Speed has no impact on the image on its way down.

# Update: after setting the default setting for set of other camera properties I've succesfully gotten the
# ISO Speed to oscilate between the minimum and maximum