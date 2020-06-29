# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 12:32:57 2020

@author: Ishan SS
"""

import cv2
import numpy as np

def empty(a):
    pass

frameWidth=480
frameHeight=320
#WebCam
cam=cv2.VideoCapture(0)
cam.set(3,frameWidth)
cam.set(4,frameHeight)


## Create Trackbar Window
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)
## Create Trackbars
cv2.createTrackbar("Hue Min","TrackBars",86,179,empty)
cv2.createTrackbar("Hue Max","TrackBars",165,179,empty)
cv2.createTrackbar("Sat Min","TrackBars",78,255,empty)
cv2.createTrackbar("Sat Max","TrackBars",255,255,empty)
cv2.createTrackbar("Val Min","TrackBars",0,255,empty)
cv2.createTrackbar("Val Max","TrackBars",255,255,empty)

while True:
    success,img=cam.read()
    imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min=cv2.getTrackbarPos("Hue Min","TrackBars")
    h_max=cv2.getTrackbarPos("Hue Max","TrackBars")
    s_min=cv2.getTrackbarPos("Sat Min","TrackBars")
    s_max=cv2.getTrackbarPos("Sat Max","TrackBars")
    v_min=cv2.getTrackbarPos("Val Min","TrackBars")
    v_max=cv2.getTrackbarPos("Val Max","TrackBars")
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    
    lower=np.array([h_min,s_min,v_min])
    upper=np.array([h_max,s_max,v_max])
    mask=cv2.inRange(imgHSV,lower,upper)
    imgResult=cv2.bitwise_and(img,img,mask=mask)
    
    mask=cv2.cvtColor(mask,cv2.COLOR_GRAY2BGR)
    hStack=np.hstack([img,mask,imgResult])
    cv2.imshow("Image Stack",hStack)

    if cv2.waitKey(1) and 0xFF == ord('q'):
        break
 
cap.release()
cv2.destroyAllWindows()
    