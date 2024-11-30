import cv2
import numpy as np

img = cv2.imread("Data\\building.jpg")
img = cv2.resize(img,(600,700))
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


def onChange(x):
    pass


cv2.namedWindow("Canny")
cv2.createTrackbar("Threshold", "Canny", 0, 255, onChange)

while True:
    a = cv2.getTrackbarPos("Threshold", "Canny")    
    print(a)
    res = cv2.Canny(img_gray, a, 255)
    cv2.imshow("Canny", res)
    k = cv2.waitKey(1000) & 0xFF
    if k == 27:
        break

#cv2.imshow("img_gray", img_gray)

cv2.destroyAllWindows()