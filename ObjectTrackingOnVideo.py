#set lh to 134
#set ls to 49

import numpy as np
import cv2 as cv
def nothing(x):
    #x is new trackbar value returned on change in trackbar position
    pass

cv.namedWindow('Tracking')
cv.createTrackbar('lh','Tracking', 0, 255, nothing)
cv.createTrackbar('ls','Tracking', 0, 255, nothing)
cv.createTrackbar('lv','Tracking', 0, 255, nothing)
cv.createTrackbar('uh','Tracking', 255, 255, nothing)
cv.createTrackbar('us','Tracking', 255, 255, nothing)
cv.createTrackbar('uv','Tracking', 255, 255, nothing)


cap = cv.VideoCapture('media/cars.mp4')

while True:
    result, frame = cap.read()
    frame = cv.resize(frame, (800,600))
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    
    l_h = cv.getTrackbarPos('lh','Tracking')
    l_s = cv.getTrackbarPos('ls','Tracking')
    l_v = cv.getTrackbarPos('lv','Tracking')

    u_h = cv.getTrackbarPos('uh','Tracking')
    u_s = cv.getTrackbarPos('us','Tracking')
    u_v = cv.getTrackbarPos('uv','Tracking')

    

    l_v = np.array([l_h, l_s, l_v])
    u_v = np.array([u_h, u_s, u_v])
    mask1 = cv.inRange(hsv,l_v,u_v)
    res = cv.bitwise_and(frame, frame,mask= mask1 )
    
   
         
    cv.imshow('image',frame)
    cv.imshow('mask',mask1)
    cv.imshow('res',res)
    k=cv.waitKey(10)
    if k == 27:
        break
cap.release()
cv.destroyAllWindows()