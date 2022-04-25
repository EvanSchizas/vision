from unittest import result
import cv2
import mediapipe as mp
import time
import HandTrackingModule as htm


#some test code now that we have established the functionality of the module

pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)
detector = htm.handDetector()
img = detector
while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img)
    if len(lmList) !=0:
        print(lmList[8]) #using the tip of index finger position to append on lmList
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img,str(int(fps)),(10,70), cv2.FONT_HERSHEY_PLAIN, 3,(255,0,255),3)
    cv2.imshow('Image', img)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()