import cv2

img = cv2.imread('media/scorpion.jpg')
img = cv2.resize(img,(250,450)) #resizing the image

# conversting to gray scale
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# converting to blurred image
img_blur = cv2.GaussianBlur(img,(7,7),0) #ksize must be odd number 3,7,9

# edge detectror
img_edges = cv2.Canny(img,300,400)

# making the edges thicker and thinner - use dilate for thicker and erode for thnner
import  numpy as np
kernel = np.ones([5,5],np.uint8) #defining the kernel

img_dilate = cv2.dilate(img_edges,kernel,iterations=1)
img_erode = cv2.erode(img_dilate,kernel,iterations=1)

#displaying images
cv2.imshow("rgbscorpion",img)
cv2.imshow("grayscorpion",img_gray)
cv2.imshow("blurscorpion",img_blur)
cv2.imshow("edgescorpion",img_edges)
cv2.imshow("dilatedscorpion",img_dilate)
cv2.imshow("erodedscorpion",img_erode)

cv2.waitKey(0)