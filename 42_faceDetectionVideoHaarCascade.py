import cv2 as cv

face_cascade = cv.CascadeClassifier('classifiers\haarcascade_frontalface_default.xml')

# img = cv.imread('media/lena.jpg')
cap = cv.VideoCapture('media/people.mp4')
while(cap.isOpened()):
    _, frame = cap.read()
    frame = cv.resize(frame, (1800,700))
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 10)
    for (x,y,w,h) in faces:
        cv.rectangle(frame, (x,y),(x+w ,y+h), (0,255,0),3)

    cv.imshow('Video', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()