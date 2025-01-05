import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('media/lena.jpg')
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

kernel = np.ones((5,5),np.float32)/25
flt2d = cv.filter2D(img,-1,kernel)
blur = cv.blur(img, [5,5])
gblur = cv.GaussianBlur(img, (5,5), 0)#'media/halftone2.jpg'
median = cv.medianBlur(img, 3)#'media/salt-and-pepper-noise.png'
bilaterl = cv.bilateralFilter(img , 9,75,75)#'media/lena.jpg'

titles  = ['image' , '2D convolution','blur', 'GaussianBlur','medianBlur','bilateralFilter']
images = [img, flt2d, blur, gblur,median,bilaterl]

for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()