import cv2
import numpy as np

i = cv2.imread("card.jpg")
img = cv2.resize(i, (649, 488))


cv2.rectangle(img, (54, 59), (591, 410), (0, 255, 0), 3)

cv2.imshow("IMG", img)
cv2.waitKey(0)