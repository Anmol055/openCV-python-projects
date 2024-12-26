import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    # channel_count = img.shape[2]
    mask_color = 255
    cv.fillPoly(mask, vertices, mask_color)
    masked_image = cv.bitwise_and(img, mask)
    return masked_image

def draw_lines(img, lines):
    blank_img = np.zeros_like(img)
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv.line(blank_img, (x1,y1), (x2,y2), (0,255,0), thickness= 3)
    img = cv.addWeighted(img, 0.8, blank_img, 1,0.0)
    return img

# def draw_lines(img, lines):
#     img = np.copy(img)
#     blank_img = np.zeros((img.shape[0],img.shape[1],img.shape[2]), np.uint8)
#     for line in lines:
#         for x1, y1, x2, y2 in line:
#             cv.line(blank_img, (x1,y1), (x2,y2), (0,255,0), thickness= 3)
#     img = cv.addWeighted(img, 0.8, blank_img, 1,0.0)
#     return img

image = cv.imread('media/Road2.jpg')
image = cv.cvtColor(image, cv.COLOR_BGR2RGB)

print(image.shape)
height = image.shape[0]
width = image.shape[1]

region_of_interest_vertices = [
    (width/3,height) , (width/2, (3.2*height)/6),(width, (4.8*height)/6) ,(width, height),]

gray_image = cv.cvtColor(image , cv.COLOR_RGB2GRAY)
median = cv.medianBlur(gray_image,5)
canny_image = cv.Canny(median, 100,120)
cropped_img = region_of_interest(canny_image, np.array([region_of_interest_vertices], np.int32))

lines = cv.HoughLinesP(cropped_img, rho = 1, theta = np.pi/180, threshold = 50, lines=np.array([]),minLineLength=10,maxLineGap=100)

img_with_lines = draw_lines(image, lines)

plt.imshow(img_with_lines)
# plt.imshow(image)
plt.show()