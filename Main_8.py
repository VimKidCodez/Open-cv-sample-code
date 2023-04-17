# More about cv2
import cv2
import numpy as np

img = cv2.imread("images/image001.jpg")
cv2.imshow("wnidow",img)

cv2.waitKey(0)
cv2.destroyAllWindows()