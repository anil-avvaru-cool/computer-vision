import numpy as np
import cv2

img = cv2.imread("Data\\col_balls.jpg",0)
#print(img.shape)


_,mask = cv2.threshold(img, 230, 255, cv2.THRESH_BINARY_INV)
kernal = np.ones((5,5),np.uint8)
#print(kernal)
e = cv2.erode(mask,kernal)

kernal1 = np.ones((3,3),np.uint8)
d = cv2.dilate(mask, kernal1)
#cv2.imshow("Dilate===", d)

"""
cv2.imshow("img1", img)
cv2.imshow("kernal", kernal)
cv2.imshow("mask", mask)
cv2.imshow("Erosion", e)
"""

from matplotlib import pyplot as plt
titles = ["img","Mask","erosion","Dilation"]
images = [img,mask,e,d]
for i in range(4):
    plt.subplot(2,2, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
    
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
