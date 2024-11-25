import numpy as np
import cv2

img = cv2.imread("Data\\col_balls.jpg",0)
_,mask = cv2.threshold(img, 230, 255, cv2.THRESH_BINARY_INV)
kernel = np.ones((3,2),np.uint8)
# Erosion first and dilation operation
o = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

#kernel = np.ones((3,3),np.uint8)
# Erosion first and dilation operation
c = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

#cv2.imshow("img1", img)
#cv2.imshow("kernal", kernel)
cv2.imshow("mask", mask)
cv2.imshow("Morph open ===", o)
cv2.imshow("Morph close ===", c)

# Difference between mask and opening
x1 = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernel)
cv2.imshow("x1", x1)

# Difference between dilation and erosion
x2 = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel)
cv2.imshow("x2", x2)

x3 = cv2.morphologyEx(mask, cv2.MORPH_BLACKHAT, kernel)
cv2.imshow("x3", x3)

cv2.waitKey(0)
cv2.destroyAllWindows()
