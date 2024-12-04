import cv2
import numpy as np

img = cv2.imread("Data\\shapes.png")
assert img is not None, "file could not be read, check with os.path.exists()"
img = cv2.resize(img,(600,700))
img1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(img1, 220, 255, cv2.THRESH_BINARY_INV)

cnts,hier = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(cnts, "len= "+str(len(cnts)))

area1 = []
for c in cnts:
    M = cv2.moments(c)
    print("moment",M)
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    
    area = cv2.contourArea(c)
    area1.append(area)
    
    if area < 10000:
        epsilon = 0.01 * cv2.arcLength(c, True)
        data = cv2.approxPolyDP(c, epsilon, True)
        hull = cv2.convexHull(data)
        x,y,w,h = cv2.boundingRect(hull)
        img = cv2.rectangle(img, (x,y),(x+w,y+h), (125,10,20),5)
        
    
        
    cv2.drawContours(img, [c], -1, (0,255,0),2)
    cv2.circle(img, (cx,cy), 7, (255,255,255),-1) # -1 solid circle
    cv2.putText(img, "Center", (cx-20,cy-20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255),2)


cv2.imshow("gray", img1)
cv2.imshow("Thresh", thresh)
cv2.imshow("Original", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
