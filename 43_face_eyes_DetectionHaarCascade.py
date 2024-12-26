import cv2 as cv

face_cascade = cv.CascadeClassifier('classifiers\haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('classifiers\haarcascade_eye_tree_eyeglasses.xml')

# img = cv.imread('media/lena.jpg')
cap = cv.VideoCapture('media/people.mp4')
while(cap.isOpened()):
    _, frame = cap.read()
    frame = cv.resize(frame, (1400,600))
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 10)
    for (x,y,w,h) in faces:
        cv.rectangle(frame, (x,y),(x+w ,y+h), (0,255,0),3)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)
    cv.imshow('Video', frame)
    if cv.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv.destroyAllWindows()