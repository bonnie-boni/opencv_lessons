# shapes and texts in cv2

import cv2
import numpy as np

img = np.zeros((600,600,3),np.uint8)
cv2.line(img,(0,0),(600,600),(255,0,255),3)

cv2.imshow("image",img)
cv2.waitKey(0)
