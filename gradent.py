import cv2
import numpy as np

img = cv2.imread("Data\\building.jpg")
img = cv2.resize(img, (600,500))
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
lap = cv2.Laplacian(img_gray, cv2.CV_64F, ksize=3)
lap = np.uint8(np.absolute(lap))

sobelX = cv2.Sobel(img_gray, cv2.CV_64F, 1, 0,ksize=3)
sobelY = cv2.Sobel(img_gray, cv2.CV_64F, 0, 1,ksize=3)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobelCombine = cv2.bitwise_or(sobelX, sobelY)

#cv2.imshow("Original", img)
#cv2.imshow("Gray", img_gray)
cv2.imshow("Lap", lap)
cv2.imshow("sobelX", sobelX)
cv2.imshow("sobelY", sobelY)
cv2.imshow("sobelCombine", sobelCombine)

cv2.waitKey()
cv2.destroyAllWindows()