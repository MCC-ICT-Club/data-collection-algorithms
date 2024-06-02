# Author: Mario Solis
# Description: In this program I go a step further with the
# live feed I created in the previous program. Here I begin
# to experiment with the temperature setting of the live feed.


import cv2 as cv

######################################################################

defaultBrightness = 100
defaultExposure = 50
defaultTemp = 23
defaultSharpness = 50

default = 0
count = 0
maxBrightness = 365
minBrightness = -365
camNum = 1
growthRate = 1
increment = 1
decrement = -1
delay = 1
quiteKey = 'q'

#######################################################################

cap = cv.VideoCapture(camNum)

cap.set(cv.CAP_PROP_TEMPERATURE, default)
cap.set(cv.CAP_PROP_BRIGHTNESS, defaultBrightness)
cap.set(cv.CAP_PROP_EXPOSURE, defaultExposure)
cap.set(cv.CAP_PROP_TEMPERATURE, defaultTemp)
cap.set(cv.CAP_PROP_SHARPNESS, defaultSharpness)

while True:
    success, img = cap.read()

    cv.imshow("pyCamTemperature", img)

    if cv.waitKey(delay) & 0xFF == ord(quiteKey):
        break

    cap.set(cv.CAP_PROP_TEMPERATURE, count)

    count += growthRate
    print(count)

    if count == minBrightness:
        growthRate = increment

    if count == maxBrightness:
        growthRate = decrement


cap.release()
cv.destroyAllWindows()

# Closing Reflection
# Its hard to tell wether or not this one is having an effect on the overall image.

# Another idea that came to me worth trying when testing out the effect of all these different properties
# would be to have a block of code that keeps certain properties locked at a default value so that when
# one is oscilating between its maximum and minimum the others not changing. That could go on to
# impact things to where more of them are causing a change in the image on the way down to their minimum.

# Update: nothing extremely noticable seems to be occuring in this shot. When observing things in this image
# i get the feeling that it would be better if I had a set of objects this was being pointed at that could more
# clearly indicate the changes in property occuring between the different settings like a white canvas to observe
# properties around the color and then a still image to observe other properties