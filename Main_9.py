# More about cv2
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("images/image001.jpg")

plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.axis("off") # Deletes the y and x axis
plt.show()