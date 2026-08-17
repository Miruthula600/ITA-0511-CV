import cv2
from google.colab.patches import cv2_imshow
img = cv2.imread("/content/yu-chin-tsai-piTEABtlR1Q-unsplash.jpg")
blur_img = cv2.GaussianBlur(img, (5, 5), 0)
print("Blurred Image")
cv2_imshow(blur_img)
