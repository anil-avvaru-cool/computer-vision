import cv2
import numpy as np

img = cv2.imread("Data\\hand.jpg")
assert img is not None, "file could not be read, check with os.path.exists()"
img = cv2.resize(img,(600,700))
img1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

blur = cv2.medianBlur(img1, 11)

ret,thresh = cv2.threshold(blur, 240, 255, cv2.THRESH_BINARY_INV)
cnts,hier = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print("cntr length ===",str( len(cnts)))
print("Hierarchy=== ", hier)

for c in cnts:
    epsilon = 0.0001 * cv2.arcLength(c, True)
    data = cv2.approxPolyDP(c, epsilon, True)
    hull = cv2.convexHull(data)
    cv2.drawContours(img, [c], -1, (50,50,200),2)
    cv2.drawContours(img, [hull], -1, (0,255,0),2)    

hull2 = cv2.convexHull(cnts[0], returnPoints= False)
defect = cv2.convexityDefects(cnts[0], hull2)

for i in range(defect.shape[0]):
    if(1==1):
        st,en,fa,ap = defect[i,0]
        print("Start, end, farthest, approx")
        print(st,en,fa,ap)
        start = tuple(c[st][0])
        end  = tuple(c[en][0])
        far  = tuple(c[fa][0])        
        #cv2.circle(img, start, 5, [250,0,5],-1)
        #cv2.circle(img, end, 5, [0,255,0],-1)
        #cv2.circle(img, far, 5, [0,0,150],-1)
        
c_max = max(cnts,key=cv2.contourArea)

extLeft = tuple(c_max[c_max[:,:,0].argmin()][0])
extRight = tuple(c_max[c_max[:,:,0].argmax()][0])

extTop = tuple(c_max[c_max[:,:,1].argmin()][0])
extBottom = tuple(c_max[c_max[:,:,1].argmax()][0])

cv2.circle(img, extLeft, 8, (255,0,255)) # pink
cv2.circle(img, extRight, 8, (0,15,255)) # Brown
cv2.circle(img, extTop, 8, (255,10,0)) # Blue
cv2.circle(img, extBottom, 8, (19,152,152)) # Green

      
    


cv2.imshow("gray", img1)
cv2.imshow("Thresh", thresh)
cv2.imshow("Original", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
























