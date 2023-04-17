import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("download.jpg",0)
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
print(img.shape)
plt.axis()
plt.show()