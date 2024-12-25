import cv2 as cv
import numpy as np

img = cv.imread('media/messi5.jpg')
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
template = cv.imread('media/football.jpg',0)

w,h = template.shape[::-1]
res = cv.matchTemplate(gray_img, template, cv.TM_CCOEFF_NORMED)
print(res)
print()
threshold = 0.9
loc = np.where(res >= threshold)
print(loc)
for pt in zip(*loc[::-1]):
    cv.rectangle(img, pt, (pt[0]+w , pt[1]+h), (0,0,255), 2)

cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()