import numpy as np
import cv2
from matplotlib import pyplot as plt
"""
# Plotting with calhist method
img = np.zeros((200,200), np.uint8)
cv2.rectangle(img, (0,100),(200,200), (255),-1)
cv2.rectangle(img, (0,50),(50,100), (127),-1)

hist = cv2.calcHist([img], [0], None, [256], [0,256])
plt.plot(hist)
plt.show()
cv2.imshow("Res",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
"""
img = cv2.imread("Data\\thor.jpg")
img = cv2.resize(img,(500,650))

"""
b,g,r = cv2.split(img)
cv2.imshow("img", img)
cv2.imshow("b", b)
cv2.imshow("g", g)
cv2.imshow("r", r)

#plt.hist(b.ravel(),256,[0,256])
plt.hist(g.ravel(),256,[0,256])
plt.hist(r.ravel(),256,[0,256])

plt.title("Colorfull image")
plt.show()
"""
hist = cv2.calcHist([img], [0], None, [256], [0,256])
plt.title("Colorful image")
plt.plot(hist)
plt.show()

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hist = cv2.calcHist([img_gray], [0], None, [256], [0,256])
plt.plot(hist)
plt.title("Gray scale")
plt.show()

equ = cv2.equalizeHist(img_gray)
res = np.hstack((img_gray,equ))
cv2.imshow("res", res)
hist1 = cv2.calcHist([equ], [0], None, [256], [0,256])
plt.plot(hist)
plt.title("Equalization")
plt.show()


#CLAHE (Contrast Limited Adaptive Histogram Equalization)
# Enchance image and handle noise
clache = cv2.createCLAHE(clipLimit=2.0,tileGridSize= (8,8))
cl1 = clache.apply(img_gray)
cv2.imshow("Clache", cl1)
hist2 = cv2.calcHist([cl1], [0], None, [256], [0,256])
plt.plot(hist)
plt.title("CLACHE")
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()






















































