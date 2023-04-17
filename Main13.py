# More about Resizing
import numpy as np
import cv2

img = cv2.imread("download.jpg")

a = img.resize(100,100)

cv2.imshow("Window",img)

cv2.waitKey(0)
cv2.destroyAllWindows()