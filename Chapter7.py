#color detection

import cv2
import numpy as np

def empty(a):
    pass

# creating the track window
cv2.namedWindow("Trackbars")
cv2.resizeWindow('Trackbars',450,350)

# creating the trackbars
cv2.createTrackbar('Hue min','Trackbars',0,179,empty)
cv2.createTrackbar('Hue max','Trackbars',179,179,empty)
cv2.createTrackbar('sat min','Trackbars',163,255,empty)
cv2.createTrackbar('sat max','Trackbars',255,255,empty)
cv2.createTrackbar('val min','Trackbars',58,255,empty)
cv2.createTrackbar('val max','Trackbars',192,255,empty)


while True:     #displays the image and its effests immediately
    img = cv2.imread('media/millena.jpg')
    img = cv2.resize(img,(450,550))
    imghue = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    # putting the track bars in action
    h_min = cv2.getTrackbarPos('Hue min','Trackbars')
    h_max = cv2.getTrackbarPos('Hue max', 'Trackbars')
    s_min = cv2.getTrackbarPos('sat min', 'Trackbars')
    s_max = cv2.getTrackbarPos('sat max', 'Trackbars')
    v_min = cv2.getTrackbarPos('val min', 'Trackbars')
    v_max = cv2.getTrackbarPos('val max', 'Trackbars')

    print(h_min,h_max,s_min,s_max,v_min,v_max)

    #applying this changes on the picture/image
    min_val = np.array([h_min,s_min,v_min])
    max_val = np.array([h_max,s_max,v_max])
    masked_img = cv2.inRange(imghue,min_val,max_val)
    result =cv2.bitwise_and(img,img,mask=masked_img)

    cv2.imshow('scorpion',img)
    cv2.imshow('scorpionhue',imghue)
    cv2.imshow('scorpionmask', masked_img)
    cv2.imshow('scorpionfinal', result)
    cv2.waitKey(1)
