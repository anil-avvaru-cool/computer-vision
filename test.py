import cv2
import numpy as np

img1 = cv2.imread("Data\\hero1.jpg")
img2 = cv2.imread("Data\\strom_breaker.jpg")

# Img2 should always be less than or equal to img1
img1 = cv2.resize(img1, (1024,650))
img2 = cv2.resize(img2, (600,650))

row, col, chan = img1.shape
print(row, col, chan)