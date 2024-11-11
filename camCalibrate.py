import cv2 as cv
import datetime
import time
import os

# Loop Count Constants
delay = 5
rest = 3
count = 0
passCounter = 0
programLength = 5
passCount = 5

# Image Save Constants
countSave = 0
moduleVal = 5
minBlur = 25
saveData = False
grayImage = False
myPath = "data/images"

# Camera Settings
camNum = 0
bufferSize = 1
imgHeight = 480
imgWidth = 720
captureProperties = [
    cv.CAP_PROP_AUTO_EXPOSURE, 
    cv.CAP_PROP_ISO_SPEED,
    cv.CAP_PROP_AUTO_WB,
    cv.CAP_PROP_HUE,
    cv.CAP_PROP_GAMMA,
    cv.CAP_PROP_AUTOFOCUS,
    cv.CAP_PROP_EXPOSURE, 
    cv.CAP_PROP_BRIGHTNESS,    
    cv.CAP_PROP_GAIN, 
    cv.CAP_PROP_SATURATION,
    cv.CAP_PROP_TEMPERATURE,
    cv.CAP_PROP_CONTRAST,
]

exposure    = cv.getTrackbarPos("Exposure", "Lighting")
brightness  = cv.getTrackbarPos("Brightness", "Lighting")
gain        = cv.getTrackbarPos("Gain", "Lighting")
saturation  = cv.getTrackbarPos("Saturation", "Lighting")
temperature = cv.getTrackbarPos("Temperature", "Lighting")
contrast    = cv.getTrackbarPos("Contrast", "Lighting")

def initialize_camera(camNum):
    cap = cv.VideoCapture(camNum, cv.CAP_V4L2)
    cap.set(cv.CAP_PROP_BUFFERSIZE, bufferSize)
    return cap

def saveDataFunc():
    global countFolder
    countFolder = 0
    while os.path.exists( myPath+ str(countFolder)):
        countFolder += 1
    os.makedirs(myPath + str(countFolder))

def setCaptureProperty(cap, prop_id, value, prop_name):
    cap.set(prop_id, value)
    actual_value = cap.get(prop_id)
    # print("Property " + str(prop_id) + " set to " + str(actual_value))
    print(f'Property {prop_name} set to {actual_value}')

def getPropName(prop_id):
    propName = ""
    match prop_id:
        case 21:
            propName = "Auto Exposure"
        case 30:
            propName = "ISO Speed"
        case 44:
            propName = "Auto WB"
        case 13:
            propName = "Hue"
        case 22:
            propName = "Gamma"
        case 39:
            propName = "Autofocus"
        case 15:
            propName = "Exposure"
        case 10:
            propName = "Brightness"
        case 14:
            propName = "Gain"
        case 12: 
            propName = "Saturation"
        case 23:
            propName = "Temperature"
        case 11:
            propName = "Contrast"
        case _:
            propName = ""
    
    return propName

def appropriateCapPropValue(cap, prop_id): 
    # Auto Exposure
    if prop_id == captureProperties[0]:
        value = cap.get(captureProperties[0])
        value = 0
    # ISO Speed
    elif prop_id == captureProperties[1]:
        value = cap.get(captureProperties[1])
        value = 1
        #value -= 1
        # print(f'Value: {value}')
    # Auto WB
    elif prop_id == captureProperties[2]:
        value = cap.get(captureProperties[2])
        value - 0
    # Hue
    elif prop_id == captureProperties[3]:
        value = cap.get(captureProperties[3])
        value = 2.0
    # Gamma
    elif prop_id == captureProperties[4]:
        value = cap.get(captureProperties[4])
        value = 3.0    
    # Autofocus
    elif prop_id == captureProperties[5]:
        value = cap.get(captureProperties[5])
        value = 3
    # Exposure
    elif prop_id == captureProperties[6]:
        value = cap.get(captureProperties[6])
        value = 900
    # Brightness
    elif prop_id == captureProperties[7]:
        value = cap.get(captureProperties[7])
        value = 220
    # Gain
    elif prop_id == captureProperties[8]:
        value = cap.get(captureProperties[8])
        value = 100
    # Saturation
    elif prop_id == captureProperties[9]:
        value = cap.get(captureProperties[9])
        value = 80
    # Temperature
    elif prop_id == captureProperties[10]:
        value = cap.get(captureProperties[10])
        value += 100
    # Contrast
    elif prop_id == captureProperties[11]:
        value = cap.get(captureProperties[11])
        value = 80

    return value

while True:
    cap = initialize_camera(camNum)
    
    for capProp in captureProperties:
        value = appropriateCapPropValue(cap, capProp)
        propName = getPropName(capProp)
        setCaptureProperty(cap, capProp, value, propName)

    time.sleep(rest)
    
    currentTime = datetime.datetime.now()
    newCycle = currentTime + datetime.timedelta(seconds = programLength)

    while True:
        
        success, img = cap.read()
        img = cv.resize(img,(imgWidth, imgHeight))    
        cv.imshow("Brightness Calibration", img)
        
        if cv.waitKey(delay) & 0xFF == ord('q'):
            break
        
        if datetime.datetime.now() >= newCycle:
            cv.destroyAllWindows()
            break
        
        if grayImage:img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
        if saveData:
            blur = cv.Laplacian(img, cv.CV_64F).var()
            if count % moduleVal ==0 and blur > minBlur:
                nowTime = time.time()
                cv.imwrite(myPath + str(countFolder) +
                        '/' + str(countSave)+"_"+ str(int(blur))+"_"+str(nowTime)+".png", img)
                countSave+=1
            count += 1
    
    cap.release()
    cap = cv.VideoCapture(camNum)
  
    #cv.SetCaptureProperty(camNum, cv.CAP_PROP_BRIGHTNESS, brightness)
    #print(cap.get(cv.CAP_PROP_BRIGHTNESS))
    #success, actual_brightness = set_brightness(cap, brightness)
    #print(f"Requested brightness: {brightness}, Actual brightness: {actual_brightness}, Success: {success}")
    
    if (cap.get(cv.CAP_PROP_AUTO_EXPOSURE) == 1.0 and cap.get(cv.CAP_PROP_EXPOSURE) > 100):
        passCounter += 1
        saveData = False
        if saveData:saveDataFunc()
        programLength = 480
    
    if passCounter == passCount:
        break
  
    cap.release()
      
cap.release()
cv.destroyAllWindows()