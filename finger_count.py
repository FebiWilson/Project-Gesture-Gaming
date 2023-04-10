import cv2
from cvzone.HandTrackingModule import HandDetector
import time

detector=HandDetector(detectionCon=0.8, maxHands=1)
time.sleep(2.0)


video=cv2.VideoCapture(0)

while True:
    ret,frame=video.read()
    hands,img=detector.findHands(frame)
  
    if hands:
        lmList=hands[0]
        fingerUp=detector.fingersUp(lmList)
        print(fingerUp)
        if sum(fingerUp)==0:
            cv2.putText(frame, 'Finger Count: 0', (20,460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)
           
        if sum(fingerUp)==1:
            cv2.putText(frame, 'Finger Count: 1', (20,460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)
           
        if sum(fingerUp)==2:
            cv2.putText(frame, 'Finger Count: 2', (20,460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)
           
        if sum(fingerUp)==3:
            cv2.putText(frame, 'Finger Count: 3', (20,460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)
          
        if sum(fingerUp)==4:
            cv2.putText(frame, 'Finger Count: 4', (20,460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)
           
        if sum(fingerUp)==5:
            cv2.putText(frame, 'Finger Count: 5', (20,460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)
            
       
    cv2.imshow("Frame",frame)
    k=cv2.waitKey(1)
    if k==ord('q'):
        break

video.release()
cv2.destroyAllWindows()

def sum(fingerUp):
    fs = 0
    for i in fingerUp:
        fs = fs + 1
    return fs

