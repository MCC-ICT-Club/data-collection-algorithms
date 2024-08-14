import cv2 as cv
import time
import datetime
import os

global countFolder

# os.environ.pop("QT_QPA_PLATFORM_PLUGIN_PATH")

camNum = 0

adjust = 50
count = 0
counter = 0
countSave = 0
moduleVal = 1
minBlur = 50
imgHeight = 480
imgWidth = 720
saveData = True
grayImage = False
myPath = "data/images"

cap = cv.VideoCapture(camNum)
cap.set(cv.CAP_PROP_BRIGHTNESS, adjust)
succes, img = cap.read()
cv.imshow("Clear Cam Settings", img)
cv.destroyAllWindows()


def saveDataFunc():
    global countFolder
    countFolder = 0
    while os.path.exists( myPath+ str(countFolder)):
        countFolder += 1
    os.makedirs(myPath + str(countFolder))

if saveData:saveDataFunc()

while True:
    time.sleep(3)
    
    current = datetime.datetime.now()
    newCycle = current + datetime.timedelta(seconds = 50)

    while True:
        
        succes, img = cap.read()
        cv.imshow("Brightness Window", img)
        
        img = cv.resize(img,(imgWidth,imgHeight))
        if grayImage:img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
        if saveData:
            blur = cv.Laplacian(img, cv.CV_64F).var()
            if count % moduleVal ==0 and blur > minBlur:
                nowTime = time.time()
                cv.imwrite(myPath + str(countFolder) +
                        '/' + str(countSave)+"_"+ str(int(blur))+"_"+str(nowTime)+".png", img)
                countSave+=1
        counter += 1
        
        if datetime.datetime.now() > newCycle:
            cv.destroyAllWindows()
            break

        
        #if cv.waitKey(5) & 0xFF == ord('q'):
         #   break
        
    adjust = adjust + 50    
    cap.set(cv.CAP_PROP_BRIGHTNESS, adjust)
    count += 1
    
    if count == 7:
        break
    
cap.release
cv.destroyAllWindows()
