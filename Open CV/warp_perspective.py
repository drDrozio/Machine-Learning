# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 20:47:12 2020

@author: Ishan SS
"""

import cv2
import numpy as np

img=cv2.imread("Resources/Cards.jpg")

width=200#img.shape[1]
height=300#img.shape[0]
## Defining Matrix of the 4 corner points
pts1=np.float32([[990,230],[863,631],[1275,320],[1148,726]])
## Corresponding to the corner points their perspective location in image
pts2=np.float32([[0,0],[0,height],[width,0],[width,height]])
## Transformation matrix
matrix= cv2.getPerspectiveTransform(pts1,pts2)
## Warp perspective
imgOutput=cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Image",img)
cv2.imshow("Warp Perspective",imgOutput)
cv2.waitKey(0)
