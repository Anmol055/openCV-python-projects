import cv2 as cv

cap = cv.VideoCapture('media/cyclist.mp4')

ret, frame1 = cap.read()
frame1 = cv.resize(frame1, (600,600))
ret, frame2 = cap.read()
frame2 = cv.resize(frame2, (600,600))

while cap.isOpened():
    diff = cv.absdiff(frame1, frame2)
    gray = cv.cvtColor(diff, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray ,(5,5), 0)
#     _ , thresh = cv.threshold(blur , 20, 255, cv.THRESH_BINARY_INV)
    canny = cv.Canny(blur, 100, 200)
#     dilated = cv.dilate(thresh, None, iterations=3)
    dilated = cv.dilate(canny, None, iterations=3)
    contours, _ = cv.findContours(dilated, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # cv.drawContours(frame1, contours, -1, (0,255,0),2)
    for contour in contours:
         (x,y,w,h) = cv.boundingRect(contour)
         if cv.contourArea(contour) < 500:
              continue
         cv.rectangle(frame1, (x,y), (x+w, y+h), (0,255,0), 2)
         cv.putText(frame1, 'Status: {}'.format('movement'), (10,20), cv.FONT_HERSHEY_SIMPLEX, 1,(0,0,255), 3)

    cv.imshow('feed', frame1)
    frame1 = frame2
    ret, frame2 = cap.read()
    frame2 = cv.resize(frame2, (600,600))

    if cv.waitKey(40) == 27:
          break
    
cv.destroyAllWindows()