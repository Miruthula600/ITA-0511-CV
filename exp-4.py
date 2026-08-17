import cv2
import numpy as np
from google.colab.patches import cv2_imshow
img = cv2.imread("/content/yu-chin-tsai-piTEABtlR1Q-unsplash.jpg")
kernel = np.ones((5,5), np.uint8)
dilated_img = cv2.dilate(img, kernel, iterations=3)
print("Dilated Image")
cv2_imshow(dilated_img)
