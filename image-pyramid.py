import cv2
import numpy as np

img = cv2.imread("Data\\avengers.jpg")
img = cv2.resize(img, (700,700))
img1 = img.copy()

for i in range(3):
    img1 = cv2.pyrDown(img1)
    cv2.imshow("Res"+str(i),img1)

cv2.waitKey()
cv2.destroyAllWindows()