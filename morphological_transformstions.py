import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('media/binary_image.png',0)
# img = cv.cvtColor(img , cv.COLOR_BGR2RGB)
_ , mask = cv.threshold(img , 100, 255, cv.THRESH_BINARY)

kernel = np.ones((5,5), np.uint8)

dilation = cv.dilate(mask , kernel , iterations=1)
erosion = cv.erode(mask , kernel , iterations=1)
opening = cv.morphologyEx(mask ,cv.MORPH_OPEN ,kernel )
closing = cv.morphologyEx(mask,cv.MORPH_CLOSE,kernel)
mg = cv.morphologyEx(mask,cv.MORPH_GRADIENT,kernel)
th = cv.morphologyEx(mask,cv.MORPH_TOPHAT,kernel)


titles = ['img', 'mask','dilation', 'erosion','opening','closing','mg','th']
images = [img , mask, dilation, erosion, opening, closing, mg, th]

for i in range(8):
    plt.subplot(2,4,i+1) , plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()