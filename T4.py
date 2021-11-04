import cv2
# RESIZING THE IMAGE

i = cv2.imread("martin.jpg")
img = cv2.resize(i, (0, 0), fx=0.5, fy=0.5)
print(img.shape)

imgResize = cv2.resize(img, (250, 140))
print(imgResize.shape)

imgCropped = img[0:200, 200:400]  # Bredth && Height

cv2.imshow("IMAGE1", img)
cv2.imshow("IMAGE2", imgResize)
cv2.imshow("Cropped Image", imgCropped)

cv2.waitKey(0)