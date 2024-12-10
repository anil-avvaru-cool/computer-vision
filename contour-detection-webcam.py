import cv2
import numpy as np

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

def onChange(x):
    pass

color_adj_win_name = "Color Adjustments"

cv2.namedWindow(color_adj_win_name, cv2.WINDOW_NORMAL)
cv2.resizeWindow(color_adj_win_name, (300,300))
cv2.createTrackbar("Thresh", color_adj_win_name, 0, 255, onChange)

cv2.createTrackbar("Lower_H", color_adj_win_name, 0, 255, onChange)
cv2.createTrackbar("Lower_S", color_adj_win_name, 0, 255, onChange)
cv2.createTrackbar("Lower_V", color_adj_win_name, 0, 255, onChange)

cv2.createTrackbar("Upper_H", color_adj_win_name, 255, 255, onChange)
cv2.createTrackbar("Upper_S", color_adj_win_name, 255, 255, onChange)
cv2.createTrackbar("Upper_V", color_adj_win_name, 255, 255, onChange)

while True:
    _,frame = cap.read()
    frame = cv2.resize(frame, (400,400))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    l_h = cv2.getTrackbarPos("Lower_H", color_adj_win_name)
    l_s = cv2.getTrackbarPos("Lower_S", color_adj_win_name)
    l_v = cv2.getTrackbarPos("Lower_V", color_adj_win_name)
    
    u_h = cv2.getTrackbarPos("Upper_H", color_adj_win_name)
    u_s = cv2.getTrackbarPos("Upper_S", color_adj_win_name)
    u_v = cv2.getTrackbarPos("Upper_V", color_adj_win_name)
    
    lower_bound = np.array([l_h, l_s, l_v])
    upper_bound = np.array([u_h, u_s, u_v])
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    
    filtr = cv2.bitwise_and(frame,frame,mask=mask)
    
    mask1 = cv2.bitwise_not(mask)
    m_g = cv2.getTrackbarPos("Thresh", color_adj_win_name)
    ret,thresh = cv2.threshold(mask1, m_g, 255, cv2.THRESH_BINARY)
    dilata = cv2.dilate(thresh, (1,1), iterations=6)
    
    cnts, heir = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for c in cnts:
        epsilon = 0.0001*cv2.arcLength(c, closed=True)
        data = cv2.approxPolyDP(c, epsilon, closed = True)
        
        hull = cv2.convexHull(data)
        cv2.drawContours(frame, [c], -1, (50,0,250),2)
        cv2.drawContours(frame, [hull], -1, (0,250,0),2)        
    
        
    cv2.imshow("mask", mask)
    cv2.imshow("Filter", filtr)
    cv2.imshow("Thresh", thresh)
    cv2.imshow("Result", frame)
    
    
    key = cv2.waitKey(25) &0xFF
    if key == 27:
        break
    
    

cap.release()
cv2.destroyAllWindows()





    




















