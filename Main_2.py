import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("download.jpg")
plt.imshow(img, cmap = 'gray')


plt.title("New window")
plt.show()
