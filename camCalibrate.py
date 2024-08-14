import cv2 as cv
import datetime
import time
import os

camNum = 0
delay = 5
rest = 3
count = 0
passCounter = 0
programLength = 5
passCount = 5
bufferSize = 1
autoExposure = 3
brightness = 0.0
isoSpeed = -1.0
exposure = 156
gain = 0.0
imgHeight = 480
imgWidth = 720

countSave = 0
moduleVal = 5
minBlur = 25
saveData = False
grayImage = False
myPath = "data/images"

def initialize_camera(camNum):
    cap = cv.VideoCapture(camNum, cv.CAP_V4L2)
    cap.set(cv.CAP_PROP_BUFFERSIZE, bufferSize)
    cap.set(cv.CAP_PROP_BRIGHTNESS, brightness)
    return cap



def saveDataFunc():
    global countFolder
    countFolder = 0
    while os.path.exists( myPath+ str(countFolder)):
        countFolder += 1
    os.makedirs(myPath + str(countFolder))
    
def set_camera_property(cap, prop_id, value):
    if cap.set(prop_id, value):
        actual_value = cap.get(prop_id)
        if actual_value == value:
            print(f"Property (prop_id) set to (actual_value)")
        else:
            print(f"Property (prop_id) could not be set to (value), actual value is (actual_value)")
    else:
        print(f"Property (prop_id) is not supported by the backend")

def set_brightness(cap, brightness):
    success = cap.set(cv.CAP_PROP_EXPOSURE, brightness)
    actual_brightness = cap.get(cv.CAP_PROP_EXPOSURE)
    return success, actual_brightness

while True:
    
    cap = initialize_camera(camNum)
    
    cap.set(cv.CAP_PROP_AUTO_EXPOSURE, autoExposure)
    actual_auto_exposure = cap.get(cv.CAP_PROP_AUTO_EXPOSURE)
    print("Actual Exposure: " + str(actual_auto_exposure))
    
    cap.set(cv.CAP_PROP_EXPOSURE, exposure)
    actual_exposure = cap.get(cv.CAP_PROP_EXPOSURE)
    print("Exposure: " + str(actual_exposure))
    
    cap.set(cv.CAP_PROP_BRIGHTNESS, brightness)
    actual_brightness = cap.get(cv.CAP_PROP_BRIGHTNESS)
    print("Brightness: " + str(actual_brightness))
    
    cap.set(cv.CAP_PROP_ISO_SPEED, isoSpeed)
    actual_iso_speed = cap.get(cv.CAP_PROP_ISO_SPEED)
    print("ISO Speed: " + str(actual_iso_speed))
    
    cap.set(cv.CAP_PROP_AUTO_WB, 1)
    actual_auto_WB = cap.get(cv.CAP_PROP_AUTO_WB)
    print("Auto WB: " + str(actual_auto_WB))
    
    cap.set(cv.CAP_PROP_GAIN, 0.0)
    actual_gain = cap.get(cv.CAP_PROP_GAIN)
    print("Gain: " + str(actual_gain))
    
    time.sleep(rest)
    
    currentTime = datetime.datetime.now()
    newCycle = currentTime + datetime.timedelta(seconds = programLength)

    while True:
        
        success, img = cap.read()
        #cap.set(cv.CAP_PROP_BRIGHTNESS, brightness)
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
    
    if actual_auto_exposure >= 1:
        autoExposure -= 1
        
    if actual_exposure > 25:
        exposure = 156
        
    if actual_gain == -1.0:
        gain += 1
        
    isoSpeed -= 1
    
    #cv.SetCaptureProperty(camNum, cv.CAP_PROP_BRIGHTNESS, brightness)
    #print(cap.get(cv.CAP_PROP_BRIGHTNESS))
    #success, actual_brightness = set_brightness(cap, brightness)
    #print(f"Requested brightness: {brightness}, Actual brightness: {actual_brightness}, Success: {success}")
    
    if (actual_auto_exposure == 1 and actual_exposure > 100):
        if actual_brightness > 20:
            brightness += 25
        passCounter += 1
        saveData = True
        if saveData:saveDataFunc()
        programLength = 480
    
    if passCounter == passCount:
        break
    
    cap.release()
      
cap.release()
cv.destroyAllWindows()
