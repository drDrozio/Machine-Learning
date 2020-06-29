# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 13:17:42 2020

@author: Ishan SS
"""

import cv2
import numpy as np

img= cv2.imread("Resources/Messi.jpg")
## Printing shape of the image (height,width,channels)
print(img.shape)
## Resizing image (width,height)
imgResize=cv2.resize(img,(300,200))
print(imgResize.shape)
## Cropping image [height,width]
imgCropped=img[:,350:850]

cv2.imshow("Original Image",img)
cv2.imshow("Resized Image",imgResize)
cv2.imshow("Cropped Image",imgCropped)
cv2.waitKey(0)
