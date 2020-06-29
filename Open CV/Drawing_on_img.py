# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 20:06:48 2020

@author: Ishan SS
"""

import cv2
import numpy as np

img=np.zeros((512,512,3),np.uint8)
## Colouring the image in the given range
img[200:300,200:300]=255,0,0
## Line (img,(starting point),(ending point),(Colour BGR mode),thickness)
cv2.line(img,(0,0),(300,300),(0,255,0),3)
cv2.line(img,(img.shape[1],0),(0,img.shape[0]),(0,0,255),3)
## Rectangle (img,(starting point),(ending point),(Colour BGR mode),thickness)
cv2.rectangle(img,(150,150),(450,450),(255,0,0),2)
## Circle (img,(starting point),radius,(Colour BGR mode),thickness)
cv2.circle(img,(400,50),30,(255,255,0),2)
## Text on image
cv2.putText(img,"OpenCV!",(350,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),1)

cv2.imshow("Image",img)
cv2.waitKey(0)
