import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
print(img.shape)
img[:] = 64, 64, 64
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 1)
cv2.rectangle(img, (100, 50), (250, 350), (0, 0, 255), 2)

cv2.circle(img, (200, 200), 40, (0, 204, 204), 3)


cv2.putText(img, "OPEN-CV", (300, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 2)

cv2.imshow("Image", img)

cv2.waitKey(0)