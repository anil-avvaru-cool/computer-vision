import cv2
import numpy as np

img = cv2.imread("Data\\shapes.png")
assert img is not None, "file could not be read, check with os.path.exists()"
img = cv2.resize(img,(600,700))
img1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)



cv2.imshow("gray", img1)
cv2.imshow("Thresh", thresh)
cv2.imshow("Original", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
