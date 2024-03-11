# resizing and cropping images in cv2

import cv2

img = cv2.imread('media/millena.jpg')
print(img.shape)

# image resizing
resized = cv2.resize(img,(680,150)) #width then height
print(resized.shape)

# cropping the image
croped = img[0:200,50:450] # height the width - are given in ranges ie from 0 - 100 == 0:100

cv2.imshow("Millena",img)
cv2.imshow("resizedMillena",resized)
cv2.imshow("croppedMillena",croped)

cv2.waitKey(0)