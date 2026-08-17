import cv2
from google.colab.patches import cv2_imshow
img = cv2.imread("/content/yu-chin-tsai-piTEABtlR1Q-unsplash.jpg")
bigger = cv2.resize(img, None, fx=2, fy=2)
smaller = cv2.resize(img, None, fx=0.5, fy=0.5)
print("Original Image")
cv2_imshow(img)
print("Original Size :", img.shape)
print("Bigger Image")
cv2_imshow(bigger)
print("Bigger Size  :", bigger.shape)
print("Smaller Image")
cv2_imshow(smaller)
print("Smaller Size :", smaller.shape)
