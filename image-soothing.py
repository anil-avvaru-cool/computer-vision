import numpy as np
import cv2

img = cv2.imread("Data\\noisy.jpg")
img = cv2.resize(img, (300,300))
cv2.imshow("Original===", img)

kernel = np.ones((5,5),np.float32)/25
h_filter = cv2.filter2D(img, -1, kernel)
cv2.imshow("Homogeneous", h_filter)

blur = cv2.blur(img,(5,5))
cv2.imshow("Blur", blur)

g_blur = cv2.GaussianBlur(img, (5,5), 0)
cv2.imshow("Gaussian", g_blur)

# size must be odd number
med_blur = cv2.medianBlur(img, 5)
cv2.imshow("Median===", med_blur)

b_filt = cv2.bilateralFilter(img, 9, 75, 75)
cv2.imshow("Bilateral===", b_filt)

cv2.waitKey(0)
cv2.destroyAllWindows()





