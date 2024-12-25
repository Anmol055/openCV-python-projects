import cv2 as cv
import numpy as np

cap = cv.VideoCapture('media/cars.mp4')

ret, frame = cap.read()
frame = cv.resize(frame, (800,600))
x,y,width,height = 392,171,55,19
track_window = (x,y,width,height)
roi = frame[y:y + height, x:x + width]
hsv_roi = cv.cvtColor(roi, cv.COLOR_BGR2HSV)
mask = cv.inRange(hsv_roi, np.array([0.0, 77.0,93.0]), np.array((180.0, 255.0, 255.0)))
roi_hist = cv.calcHist([hsv_roi], [0], mask, [180],[0,180])
cv.normalize(roi_hist, roi_hist, 0, 255, cv.NORM_MINMAX)

termination_crit = (cv.TERM_CRITERIA_EPS| cv.TERM_CRITERIA_COUNT, 10, 1)
cv.imshow('roi',roi)

while(cap.isOpened()):
    ret , frame = cap.read()
    frame = cv.resize(frame, (800,600))

    hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    dst = cv.calcBackProject([hsv_frame], [0], roi_hist, [0,180], 1)
    ret , track_window = cv.CamShift(dst ,track_window, termination_crit)
    # print(ret)
    pts = cv.boxPoints(ret)
    # print(pts)
    pts = np.int64(pts)
    final_image = cv.polylines(frame, [pts], True, (0,255,0),2)
    cv.imshow('dst', dst)
    cv.imshow('final_image', final_image)
    
    if cv.waitKey(10) & 0xff == 27:
        break

cap.release()
cv.destroyAllWindows()