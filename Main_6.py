# Cropping an image
import io

import cv2
import numpy as np
from matplotlib import pyplot as plt
"""
img =cv2.imread("download.jpg")
roi = img[700:10,700:10,700:10]
plt.imshow(cv2.cvtColor(roi,cv2.COLOR_BGR2RGB))
print(img.shape)
plt.show()
"""

img = cv2.imread("C:\\Users\\LENOVO\\Desktop\\code\code\\download.jpg")
roi = img[1500:2500,1000:2000]
plt.imshow(img,cv2.cvtColor(roi, cv2.COLOR_BGR2RGB))
plt.title('man')
plt.axis('off')
plt.show()
