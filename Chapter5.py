# Straigtenning an image

import cv2
import numpy as np

img = cv2.imread('media/images.jpeg')
img = cv2.resize(img,(450,450))
print(img.shape)

width,height = 350,350
pts1 = np.float32([[134,44],[339,52],[131,404],[342,387]])       #actual edges of the picture
pts2 = np.float32([[0,0],[height,0],[0,width],[height,width]])

#get the matrix of the image then combine the two
matrix = cv2.getPerspectiveTransform(pts1,pts2)
rectified = cv2.warpPerspective(img,matrix,(width,height))
print(rectified.shape)

cv2.imshow("jack",img)
cv2.imshow("rect_jack",rectified)
cv2.waitKey(0)
