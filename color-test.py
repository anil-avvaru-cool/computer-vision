import cv2
import numpy as np

# Create a new image with a white background
width = 2
height = 3
image = np.zeros((height, width,3), np.uint8)

#image[:] = (50, 100, 255)  # White color in BGR format
print(image)

# Display the image
cv2.imshow("White Background", image)
cv2.waitKey(0)
cv2.destroyAllWindows()