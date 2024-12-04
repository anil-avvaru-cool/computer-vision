import cv2
import numpy as np

img = cv2.imread("Data\\rectangle.jpg")
#img = cv2.resize(img, (300,300))
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(img1, 30, 255, 0)


cnts,hier = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(cnts, "len= "+str(len(cnts)))

# Third param -1 means all contours
img = cv2.drawContours(img, cnts, -1, (176,10,15),2)

cv2.imshow("gray", img1)
cv2.imshow("Thresh", thresh)
cv2.imshow("Original", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
