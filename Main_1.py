from matplotlib import pyplot as plt
import numpy as np
import cv2

img = cv2.imread("download.jpg")

cv2.imshow("window",img)


cv2.waitKey(0)