# Joining images
# becomes handy while printing diffrent images

import cv2
import numpy as np

img = cv2.imread('media/8a4a4d2b1beb7bd131f78fb5c3493c50.jpg')
img = cv2.resize(img,(450,550))
imggray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

imghor = np.hstack([img,img])
imgver = np.vstack([img,img])

cv2.imshow("casie cage",img)
cv2.imshow("casie cageh",imghor)
cv2.imshow("casie cagev",imgver)

cv2.waitKey(0)