import cv2
import numpy as np
import imutils

img = cv2.imread('images/image001.jpg')

hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

lower_range = np.array([110,50,50]) # a dark color
upper_range = np.array([130,255,255]) # a grey color or blackj - white meadian comour

mask = cv2.inRange(hsv, lower_range, upper_range) # returns a binary image which is white where the colors are detected and "0" otherwise, # Sorce :opencv

cv2.imshow('Image', img)  # origianl
cv2.imshow('Masked', mask) # masked (only blue shown as white)

while True:
   k = cv2.waitKey(5) & 0xFF
   if k == 27:
      break

cv2.destroyAllWindows()