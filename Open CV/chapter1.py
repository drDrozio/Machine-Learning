# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 23:39:36 2020

@author: Ishan SS
"""

import cv2
import numpy as np

import os
os.path.isfile("Resources/Ramu.jpg")

## Store image into img variable and show as output
img= cv2.imread("Resources/Messi.jpg")
cv2.imshow("Output",img)
cv2.waitKey(0)

kernel=np.ones((5,5),np.uint8)
## Convert RGB to Gratyscale
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
## Blurring the grayscale image
imgBlur=cv2.GaussianBlur(imgGray,(7,7),0)
## Edge detection
imgCanny=cv2.Canny(img,100,100)
imgCanny1=cv2.Canny(img,200,200)
## Filling the gaps of the canny image. Defining kernel size for that
imgDialation=cv2.dilate(imgCanny,kernel,iterations=1)
## Opposite of dialation-erroding
imgEroded=cv2.erode(imgDialation,kernel,iterations=1)

cv2.imshow("Gray Image",imgGray)
cv2.imshow("Blur Image",imgBlur)
cv2.imshow("Canny Image",imgCanny)
cv2.imshow("Canny Image1",imgCanny1)
cv2.imshow("Dialation Image",imgDialation)
cv2.imshow("Eroded Image",imgEroded)
cv2.waitKey(0)


## Importing video
cap=cv2.VideoCapture("Resources/JP_LOL.mp4")
## Video has to accessed frame by frame. Therefor while loop
while True:
    success, vd=cap.read()
    cv2.imshow("Video",vd)
    ## Exit console if 'q' is pressed
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
    
## Web cam
cam=cv2.VideoCapture(0)
cam.set(3,640)
cam.set(4,480)
cam.set(10,100)
## Video has to accessed frame by frame. Therefor while loop
while True:
    success2, web_cam=cam.read()
    cv2.imshow("Video",web_cam)
    ## Exit console if 'q' is pressed
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()