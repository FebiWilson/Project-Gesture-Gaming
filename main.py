import time
import tkinter as tk

import cv2
import mediapipe as mp
from pyparsing import null_debug_action

from directkeys import (PressKey, ReleaseKey, down_pressed, left_pressed,
                        right_pressed, space_pressed, up_pressed)


def process_video():
    global is_running
    
    if is_running:
        video=cv2.VideoCapture(0)
        break_key_pressed=down_pressed
        accelerato_key_pressed=space_pressed
        third_button=right_pressed
        fourth_button=left_pressed

        time.sleep(2.0)
        current_key_pressed = set()

        mp_draw=mp.solutions.drawing_utils
        mp_hand=mp.solutions.hands


        tipIds=[4,8,12,16,20]
        with mp_hand.Hands(min_detection_confidence=0.5,
                    min_tracking_confidence=0.5) as hands:
            while is_running:
                keyPressed = False
                break_pressed=False
                accelerator_pressed=False
                lsteer_pressed=False
                rsteer_pressed=False
                key_count=0
                key_pressed=0
                ret,image=video.read()
                image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                image.flags.writeable=False
                results=hands.process(image)
                image.flags.writeable=True
                image=cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                lmList=[]
                if results.multi_hand_landmarks:
                    for hand_landmark in results.multi_hand_landmarks:
                        myHands=results.multi_hand_landmarks[0]
                        for id, lm in enumerate(myHands.landmark):
                            h,w,c=image.shape
                            cx,cy= int(lm.x*w), int(lm.y*h)
                            lmList.append([id,cx,cy])
                        mp_draw.draw_landmarks(image, hand_landmark, mp_hand.HAND_CONNECTIONS)
                fingers=[]
                if len(lmList)!=0:
                    if lmList[tipIds[0]][1] > lmList[tipIds[0]-1][1]:
                        fingers.append(1)
                    else:
                        fingers.append(0)
                    for id in range(1,5):
                        if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]:
                            fingers.append(1)
                        else:
                            fingers.append(0)
                    total=fingers.count(1)
                    if total==0:
                        cv2.rectangle(image, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
                        cv2.putText(image, "BRAKE", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                            2, (255, 0, 0), 5)
                        PressKey(break_key_pressed)
                        break_pressed=True
                        current_key_pressed.add(break_key_pressed)
                        key_pressed=break_key_pressed
                        keyPressed = True
                        key_count=key_count+1
                    elif total==5:
                        cv2.rectangle(image, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
                        cv2.putText(image, "POWER", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                            2, (255, 0, 0), 5)
                        PressKey(accelerato_key_pressed)
                        key_pressed=accelerato_key_pressed
                        accelerator_pressed=True
                        keyPressed = True
                        current_key_pressed.add(accelerato_key_pressed)
                        key_count=key_count+1
                    elif total==3:
                        cv2.rectangle(image, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
                        cv2.putText(image, "RIGHT", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                            2, (255, 0, 0), 5)
                        PressKey(third_button)
                        key_pressed=third_button
                        lsteer_pressed=True
                        keyPressed = True
                        current_key_pressed.add(third_button)
                        key_count=key_count+1
                    elif total==2:
                        cv2.rectangle(image, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
                        cv2.putText(image, "LEFT", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                            2, (255, 0, 0), 5)
                        PressKey(fourth_button)
                        key_pressed=fourth_button
                        rsteer_pressed=True
                        keyPressed = True
                        current_key_pressed.add(fourth_button)
                        key_count=key_count+1
                if not keyPressed and len(current_key_pressed) != 0:
                    for key in current_key_pressed:
                        ReleaseKey(key)
                    current_key_pressed = set()
                elif key_count==1 and len(current_key_pressed)==2:    
                    for key in current_key_pressed:             
                        if key_pressed!=key:
                            ReleaseKey(key)
                    current_key_pressed = set()
                    for key in current_key_pressed:
                        ReleaseKey(key)
                    current_key_pressed = set()


                    # if lmList[8][2] < lmList[6][2]:
                    #     print("Open")
                    # else:
                    #     print("Close")
                cv2.imshow("Frame",image)
                k=cv2.waitKey(1)
                if k=='q':
                    stop
                    break
    video.release()
    cv2.destroyAllWindows()
window = tk.Tk()
window.title("Hand Gesture Control")
window.geometry("400x200")

is_running=False

def start():
    global is_running
    is_running = True
    window.after(1, process_video)

def stop():
    global is_running
    is_running = False
    print("stop")

start_button = tk.Button(window, text="Start", command=start)
start_button.pack(side="left", padx=10)

stop_button = tk.Button(window, text="Stop", command=stop)
stop_button.pack(side="left", padx=10)

window.mainloop()

