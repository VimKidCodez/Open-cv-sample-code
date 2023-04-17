# On threshholding
import numpy as np
import cv2

img = cv2.imread("image001.jpg")

ret, thresholding = cv2.threshold(img,29,255,cv2.THRESH_BINARY)
cv2.imshow("Windows",ret)

cv2.waitKey(0)
cv2.destroyAllWindows()