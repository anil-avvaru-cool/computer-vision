import cv2
import numpy as np

img1 = cv2.imread("Data\\hero1.jpg")
img2 = cv2.imread("Data\\strom_breaker.jpg")

# Img2 should always be less than or equal to img1
img1 = cv2.resize(img1, (1024,650))
img2 = cv2.resize(img2, (600,650))

row, col, chan = img2.shape
print(row,col,chan)

roi = img1[0:row,0:col]
img_gry = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Create mask using thresholding
_, mask = cv2.threshold(img_gry, 50, 255, cv2.THRESH_BINARY)

# remove background
mask_inv = cv2.bitwise_not(mask)

#put mask into roi
img1_bg = cv2.bitwise_and(roi, roi,mask = mask_inv)

# extract region of figure from original image
img2_fg = cv2.bitwise_and(img2, img2, mask = mask)

res = cv2.add(img1_bg, img2_fg)

final = img1

final[0:row,0:col] = res
#cv2.imshow("Thor", img1)
#cv2.imshow("Strom Breaker", img2)
#cv2.imshow("ROI===", roi)
#cv2.imshow("step 1 gray", img_gry)
#cv2.imshow("step 2 mask", mask)
#cv2.imshow("step 3 mask inv", mask_inv)
cv2.imshow("step 4 mask img1 bg", img1_bg)
cv2.imshow("step 5 bitwise and", img2_fg)
cv2.imshow("result", res)
cv2.imshow("final", final)

cv2.waitKey(0)
cv2.destroyAllWindows()