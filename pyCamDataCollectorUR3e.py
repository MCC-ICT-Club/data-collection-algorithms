import cv2 as cv
import time
import threading

def adjustingCam():
    
    cameraSettings = [cv.CAP_PROP_EXPOSURE, cv.CAP_PROP_BRIGHTNESS]
    windowTitles = ["pyCamDataCollector_Exposure", "pyCamDataCollector_Brightness"]

    camNum = 0
    delay = 5
    quiteKey = 'q'
    brightnessManual = 0
    count = 0
    
    cap = cv.VideoCapture(camNum)

    cap.set(cameraSettings[1], 20)
    while True:
        succes, img = cap.read()
        cv.imshow(windowTitles[1], img)

        cap.set(cameraSettings[1], brightnessManual)

        if cv.waitKey(delay) & 0xFF == ord('w'):
            cv.destroyAllWindows()
            brightnessManual += 50
            print(brightnessManual)
            
        if cv.waitKey(delay) & 0xFF == ord('s'):
            cv.destroyAllWindows()
            brightnessManual -= 50
            print(brightnessManual)

        if cv.waitKey(delay) & 0xFF == ord(quiteKey):
            cv.destroyAllWindows()
            cap.set(cv.CAP_PROP_EXPOSURE, 0)
            cap.set(cv.CAP_PROP_BRIGHTNESS, 0)
            break
        timer.start()
        count += 1
        brightnessManual += 50
        print(brightnessManual)
        cv.destroyAllWindows()



    cap.release()
    cv.destroyAllWindows()

timer = threading.Timer(5, adjustingCam)
adjustingCam()