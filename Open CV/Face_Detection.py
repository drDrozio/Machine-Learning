# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 11:16:17 2020

@author: Ishan SS
"""

import cv2
import numpy as np

faceCascade=cv2.CascadeClassifier('Resources/haarcascade_frontalface_default.xml')
img=cv2.imread('Resources/SicMundus.jpg')
imgResize=cv2.resize(img,(1000,600))
imgGray=cv2.cvtColor(imgResize,cv2.COLOR_BGR2GRAY)

faces=faceCascade.detectMultiScale(imgGray,1.1,4)
for (x,y,w,h) in faces:
    cv2.rectangle(imgResize,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow("Image",imgResize)
cv2.waitKey(0)