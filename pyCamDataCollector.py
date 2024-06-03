# Author: Mario Solis
# Description: In this program I take things even further after having
# made multiple programs giving me the ability to observe the overall
# on an image between a variety of different varying settings. In this
# program I merge the settings that had the most impact on the image
# into a single program that alternates between the different settings
# when collecting images to improve my data collection methodology and
# resulting cascade for object detection

import cv2 as cv

######################################################################

defaultBrightness = 100
defaultExposure = 50
defaultTemp = 23
defaultSharpness = 50
defaultContrast = 50
defaultSaturation = 65
defaultISO_Speed = 30
defaultHue = 50
defaultGamma = 50

oscillatingValues = [0, 265,  -365, 365,  0, 365, -125, 125, -365, 365, 0, 60, -165, 165, 0, 365]

default = 0
count = 0
tally = 0
maxValue = 265
minValue = 0
camNum = 1
growthRate = 1
increment = 1
decrement = -1
delay = 1
quiteKey = 'q'

#######################################################################

cap = cv.VideoCapture(camNum)


cap.set(cv.CAP_PROP_EXPOSURE, defaultExposure)
cap.set(cv.CAP_PROP_BRIGHTNESS, defaultBrightness)
cap.set(cv.CAP_PROP_TEMPERATURE, defaultTemp)
cap.set(cv.CAP_PROP_SHARPNESS, defaultSharpness)
cap.set(cv.CAP_PROP_CONTRAST, defaultContrast)
cap.set(cv.CAP_PROP_SATURATION, defaultSaturation)
cap.set(cv.CAP_PROP_ISO_SPEED, defaultISO_Speed)
cap.set(cv.CAP_PROP_HUE, defaultHue)
cap.set(cv.CAP_PROP_GAMMA, defaultGamma)

while True:
    success, img = cap.read()

    cv.imshow("pyCamDataCollector_Brightness", img)

    if tally == 0:
        minValue = oscillatingValues[0]
        maxValue = oscillatingValues[1]

    if count == maxValue:
        growthRate = decrement
        tally += 1

    if count == minValue:
        growthRate = increment
        tally += 1

    count += growthRate
    print(count)

    cap.set(cv.CAP_PROP_BRIGHTNESS, count)

    if cv.waitKey(delay) & 0xFF == ord(quiteKey) or tally == 4:
        tally = 0
        cv.destroyAllWindows()
        cap.set(cv.CAP_PROP_EXPOSURE, defaultExposure)
        cap.set(cv.CAP_PROP_BRIGHTNESS, defaultBrightness)
        cap.set(cv.CAP_PROP_TEMPERATURE, defaultTemp)
        cap.set(cv.CAP_PROP_SHARPNESS, defaultSharpness)
        cap.set(cv.CAP_PROP_CONTRAST, defaultContrast)
        cap.set(cv.CAP_PROP_SATURATION, defaultSaturation)
        cap.set(cv.CAP_PROP_ISO_SPEED, defaultISO_Speed)
        cap.set(cv.CAP_PROP_HUE, defaultHue)
        cap.set(cv.CAP_PROP_GAMMA, defaultGamma)
        break

while True:
    success, img = cap.read()

    cv.imshow("pyCamDataCollector_Temperature", img)

    if tally == 0:
        minValue = oscillatingValues[2]
        maxValue = oscillatingValues[3]

    if count == maxValue:
        growthRate = decrement
        tally += 1

    if count == minValue:
        growthRate = increment
        tally += 1

    count += growthRate
    print(count)

    cap.set(cv.CAP_PROP_TEMPERATURE, count)

    if cv.waitKey(delay) & 0xFF == ord(quiteKey) or tally == 4:
        tally = 0
        cv.destroyAllWindows()
        cap.set(cv.CAP_PROP_EXPOSURE, defaultExposure)
        cap.set(cv.CAP_PROP_BRIGHTNESS, defaultBrightness)
        cap.set(cv.CAP_PROP_TEMPERATURE, defaultTemp)
        cap.set(cv.CAP_PROP_SHARPNESS, defaultSharpness)
        cap.set(cv.CAP_PROP_CONTRAST, defaultContrast)
        cap.set(cv.CAP_PROP_SATURATION, defaultSaturation)
        cap.set(cv.CAP_PROP_ISO_SPEED, defaultISO_Speed)
        cap.set(cv.CAP_PROP_HUE, defaultHue)
        cap.set(cv.CAP_PROP_GAMMA, defaultGamma)
        break

while True:
    success, img = cap.read()

    cv.imshow("pyCamDataCollector_Sharpness", img)

    if tally == 0:
        minValue = oscillatingValues[4]
        maxValue = oscillatingValues[5]

    if count == maxValue:
        growthRate = decrement
        tally += 1

    if count == minValue:
        growthRate = increment
        tally += 1

    count += growthRate
    print(count)

    cap.set(cv.CAP_PROP_SHARPNESS, count)

    if cv.waitKey(delay) & 0xFF == ord(quiteKey) or tally == 4:
        tally = 0
        cv.destroyAllWindows()
        cap.set(cv.CAP_PROP_EXPOSURE, defaultExposure)
        cap.set(cv.CAP_PROP_BRIGHTNESS, defaultBrightness)
        cap.set(cv.CAP_PROP_TEMPERATURE, defaultTemp)
        cap.set(cv.CAP_PROP_SHARPNESS, defaultSharpness)
        cap.set(cv.CAP_PROP_CONTRAST, defaultContrast)
        cap.set(cv.CAP_PROP_SATURATION, defaultSaturation)
        cap.set(cv.CAP_PROP_ISO_SPEED, defaultISO_Speed)
        cap.set(cv.CAP_PROP_HUE, defaultHue)
        cap.set(cv.CAP_PROP_GAMMA, defaultGamma)
        break

while True:
    success, img = cap.read()

    cv.imshow("pyCamDataCollector_Contrast", img)

    if tally == 0:
        minValue = oscillatingValues[6]
        maxValue = oscillatingValues[7]

    if count == maxValue:
        growthRate = decrement
        tally += 1

    if count == minValue:
        growthRate = increment
        tally += 1

    count += growthRate
    print(count)

    cap.set(cv.CAP_PROP_CONTRAST, count)

    if cv.waitKey(delay) & 0xFF == ord(quiteKey) or tally == 4:
        tally = 0
        cv.destroyAllWindows()
        cap.set(cv.CAP_PROP_EXPOSURE, defaultExposure)
        cap.set(cv.CAP_PROP_BRIGHTNESS, defaultBrightness)
        cap.set(cv.CAP_PROP_TEMPERATURE, defaultTemp)
        cap.set(cv.CAP_PROP_SHARPNESS, defaultSharpness)
        cap.set(cv.CAP_PROP_CONTRAST, defaultContrast)
        cap.set(cv.CAP_PROP_SATURATION, defaultSaturation)
        cap.set(cv.CAP_PROP_ISO_SPEED, defaultISO_Speed)
        cap.set(cv.CAP_PROP_HUE, defaultHue)
        cap.set(cv.CAP_PROP_GAMMA, defaultGamma)
        break

while True:
    success, img = cap.read()

    cv.imshow("pyCamDataCollector_Saturation", img)

    if tally == 0:
        minValue = oscillatingValues[8]
        maxValue = oscillatingValues[9]

    if count == maxValue:
        growthRate = decrement
        tally += 1

    if count == minValue:
        growthRate = increment
        tally += 1

    count += growthRate
    print(count)

    cap.set(cv.CAP_PROP_SATURATION, count)

    if cv.waitKey(delay) & 0xFF == ord(quiteKey) or tally == 4:
        tally = 0
        cv.destroyAllWindows()
        cap.set(cv.CAP_PROP_EXPOSURE, defaultExposure)
        cap.set(cv.CAP_PROP_BRIGHTNESS, defaultBrightness)
        cap.set(cv.CAP_PROP_TEMPERATURE, defaultTemp)
        cap.set(cv.CAP_PROP_SHARPNESS, defaultSharpness)
        cap.set(cv.CAP_PROP_CONTRAST, defaultContrast)
        cap.set(cv.CAP_PROP_SATURATION, defaultSaturation)
        cap.set(cv.CAP_PROP_ISO_SPEED, defaultISO_Speed)
        cap.set(cv.CAP_PROP_HUE, defaultHue)
        cap.set(cv.CAP_PROP_GAMMA, defaultGamma)
        break

while True:
    success, img = cap.read()

    cv.imshow("pyCamDataCollector_ISO_Speed", img)

    if tally == 0:
        minValue = oscillatingValues[10]
        maxValue = oscillatingValues[11]

    if count == maxValue:
        growthRate = decrement
        tally += 1

    if count == minValue:
        growthRate = increment
        tally += 1

    count += growthRate
    print(count)

    cap.set(cv.CAP_PROP_ISO_SPEED, count)

    if cv.waitKey(delay) & 0xFF == ord(quiteKey) or tally == 4:
        tally = 0
        cv.destroyAllWindows()
        cap.set(cv.CAP_PROP_EXPOSURE, defaultExposure)
        cap.set(cv.CAP_PROP_BRIGHTNESS, defaultBrightness)
        cap.set(cv.CAP_PROP_TEMPERATURE, defaultTemp)
        cap.set(cv.CAP_PROP_SHARPNESS, defaultSharpness)
        cap.set(cv.CAP_PROP_CONTRAST, defaultContrast)
        cap.set(cv.CAP_PROP_SATURATION, defaultSaturation)
        cap.set(cv.CAP_PROP_ISO_SPEED, defaultISO_Speed)
        cap.set(cv.CAP_PROP_HUE, defaultHue)
        cap.set(cv.CAP_PROP_GAMMA, defaultGamma)
        break

while True:
    success, img = cap.read()

    cv.imshow("pyCamDataCollector_Hue", img)

    if tally == 0:
        minValue = oscillatingValues[12]
        maxValue = oscillatingValues[13]

    if count == maxValue:
        growthRate = decrement
        tally += 1

    if count == minValue:
        growthRate = increment
        tally += 1

    count += growthRate
    print(count)

    cap.set(cv.CAP_PROP_HUE, count)

    if cv.waitKey(delay) & 0xFF == ord(quiteKey) or tally == 4:
        tally = 0
        cv.destroyAllWindows()
        cap.set(cv.CAP_PROP_EXPOSURE, defaultExposure)
        cap.set(cv.CAP_PROP_BRIGHTNESS, defaultBrightness)
        cap.set(cv.CAP_PROP_TEMPERATURE, defaultTemp)
        cap.set(cv.CAP_PROP_SHARPNESS, defaultSharpness)
        cap.set(cv.CAP_PROP_CONTRAST, defaultContrast)
        cap.set(cv.CAP_PROP_SATURATION, defaultSaturation)
        cap.set(cv.CAP_PROP_ISO_SPEED, defaultISO_Speed)
        cap.set(cv.CAP_PROP_HUE, defaultHue)
        cap.set(cv.CAP_PROP_GAMMA, defaultGamma)
        break

while True:
    success, img = cap.read()

    cv.imshow("pyCamDataCollector_Gamma", img)

    if tally == 0:
        minValue = oscillatingValues[14]
        maxValue = oscillatingValues[15]

    if count == maxValue:
        growthRate = decrement
        tally += 1

    if count == minValue:
        growthRate = increment
        tally += 1

    count += growthRate
    print(count)

    cap.set(cv.CAP_PROP_GAMMA, count)

    if cv.waitKey(delay) & 0xFF == ord(quiteKey) or tally == 4:
        tally = 0
        cv.destroyAllWindows()
        cap.set(cv.CAP_PROP_EXPOSURE, defaultExposure)
        cap.set(cv.CAP_PROP_BRIGHTNESS, defaultBrightness)
        cap.set(cv.CAP_PROP_TEMPERATURE, defaultTemp)
        cap.set(cv.CAP_PROP_SHARPNESS, defaultSharpness)
        cap.set(cv.CAP_PROP_CONTRAST, defaultContrast)
        cap.set(cv.CAP_PROP_SATURATION, defaultSaturation)
        cap.set(cv.CAP_PROP_ISO_SPEED, defaultISO_Speed)
        cap.set(cv.CAP_PROP_HUE, defaultHue)
        cap.set(cv.CAP_PROP_GAMMA, defaultGamma)
        break



cap.release()
cv.destroyAllWindows()