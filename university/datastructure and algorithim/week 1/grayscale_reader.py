from PIL import Image, ImageOps
import numpy as np
import cv2

image = cv2.imread('grayscale-image-1024x682.jpg')
img_matrix = np.array(image)
print(img_matrix)