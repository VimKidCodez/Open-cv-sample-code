# Extract average color
import cv2
import numpy as np


img = cv2.imread("image001.jpg")



def averagecolor(image):
    return np.mean(image,axis=(0,1))

print(averagecolor(img))