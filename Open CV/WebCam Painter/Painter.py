# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 12:22:13 2020

@author: Ishan SS
"""
import cv2
import numpy as np

frameWidth=640
frameHeight=480

#WebCam
cam=cv2.VideoCapture(0)
cam.set(3,frameWidth)
cam.set(4,frameHeight)
cam.set(10,150)

myColors=[[27,77,74,255,0,255]]
myPoints=[]

def findColor(img,myColor):
    imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    newPoints=[]
    for color in myColors:
        lower=np.array([color[0],color[2],color[4]])
        upper=np.array([color[1],color[3],color[5]])
        mask=cv2.inRange(imgHSV,lower,upper)
        #Test
        #cv2.imshow("Image",mask)
        x,y=getContours(mask)
        if x!=0 and y!=0:
            newPoints.append([x,y])
        cv2.circle(imgResult,(x,y),10,(255,0,0),cv2.FILLED)
    return newPoints
   
def getContours(img):
    contours,hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h=0,0,0,0
    for cnt in contours:
        area=cv2.contourArea(cnt)
        if area>500:
            cv2.drawContours(imgResult,cnt,-1,(0,0,0),3)
            perimeter=cv2.arcLength(cnt,True)
            approx=cv2.approxPolyDP(cnt,0.02*perimeter,True)
            x,y,w,h=cv2.boundingRect(approx) 
    return x+w//2,y

def drawOnCanvas(myPoints):
    for point in myPoints:
        cv2.circle(imgResult,(point[0],point[1]),10,(0,255,0),cv2.FILLED)

## Video has to accessed frame by frame. Therefor while loop
while True:
    success2, web_cam=cam.read()
    imgResult=web_cam.copy()
    newPoints=findColor(web_cam,myColors)
    if(len(newPoints)!=0):
        for newP in newPoints:
            myPoints.append(newP)
    if(len(myPoints)!=0):
        drawOnCanvas(myPoints)
        
    cv2.imshow("Result",imgResult)
    cv2.imshow("Video",web_cam)
    ## Exit console if 'q' is pressed
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()