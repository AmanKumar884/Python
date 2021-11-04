import cv2
import numpy as np

img = cv2.imread("img1.jpg")
half = cv2.resize(img, (0, 0), fx=0.3, fy=0.3)

kernel = np.ones((5, 5), np.uint8)

imgGray = cv2.cvtColor(half, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
imgCanny = cv2.Canny(imgGray, 100, 100)
imgDiala= cv2.dilate(imgCanny, kernel, iterations=1)  # if iteration increase then white space also increses
imgErode = cv2.erode(imgDiala, kernel, iterations=1)

cv2.imshow("GRAY", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dilation Image", imgDiala)
cv2.imshow("Erode Image", imgErode)

cv2.waitKey(0)