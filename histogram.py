import numpy as np
import cv2
from matplotlib import pyplot as plt

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
