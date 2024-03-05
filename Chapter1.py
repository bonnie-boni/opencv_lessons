import cv2

print("Import successful...")

# reading images

img = cv2.imread('media/8a4a4d2b1beb7bd131f78fb5c3493c50.jpg')
cv2.imshow('Casie Cage',img)
cv2.waitKey(0) #this dectates the time that the image will be displayed in miliseconds - 0 shows infinite

# reading videos
# videos are sequence of images- thus to display we'll use loops

vid = cv2.VideoCapture("media/CAIN - I'm So Blessed (Official Music Video).mp4")

while True:
    success,img = vid.read()
    cv2.imshow("Am so blessed",img)

    # to break out of the loop - lets set it to key q to quit
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

# for using webcam is very similar to reading videos only some changes

cam = cv2.VideoCapture(0) #0 will use cam in your machine or else add the webcam id
cam.set(3,640)#setting cam size (widthidno=3,size)
cam.set(4,480)#(heightidno=4,size)
cam.set(10,40)#setting brightness

while True:
    success,img = cam.read()
    cv2.imshow("Am so blessed",img)

    # to break out of the loop - lets set it to key q to quit
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break