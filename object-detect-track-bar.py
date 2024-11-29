import cv2
import numpy as np

frame = cv2.imread("Data\\color_balls.jpg")
frame = cv2.resize(frame, (600,400))

def onChange(x):
    pass

winname = "Color Adjustments"
cv2.namedWindow(winname)
lower_h = "Lower_H"
lower_s = "Lower_S"
lower_v = "Lower_V"
Upper_H = "Upper_H"
Upper_S = "Upper_S"
Upper_V = "Upper_V"
cv2.createTrackbar(lower_h, winname, 0, 255, onChange)
cv2.createTrackbar(lower_s, winname, 0, 255, onChange)
cv2.createTrackbar("Lower_V", winname, 0, 255, onChange)

cv2.createTrackbar(Upper_H, winname, 255, 255, onChange)
cv2.createTrackbar(Upper_S, winname, 255, 255, onChange)
cv2.createTrackbar(Upper_V, winname, 255, 255, onChange)

while True:
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    l_h = cv2.getTrackbarPos(lower_h, winname)
    l_s = cv2.getTrackbarPos(lower_s, winname)
    l_v = cv2.getTrackbarPos(lower_v, winname)
    
    u_h = cv2.getTrackbarPos(Upper_H, winname)
    u_s = cv2.getTrackbarPos(Upper_S, winname)
    u_v = cv2.getTrackbarPos(Upper_V, winname)
    
    lowerb = np.array([l_h,l_s,l_v])
    upperb = np.array([u_h,u_s,u_v])
    
    mask = cv2.inRange(hsv, lowerb, upperb)
    res = cv2.bitwise_and(frame, frame, mask = mask)
    cv2.imshow("Original Frame", frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("Res", res)
    
    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()





















