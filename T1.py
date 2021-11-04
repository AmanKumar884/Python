# LOADING IMAGES
import cv2  # computer vision
print("package imported!!")

img = cv2.imread("img1.jpg", 0)
# 1- loads a color image
# 0 - loads image in grayscale mode
# -1 - loads image as such including alpha channel

cv2.imshow("Output", img)

k = cv2.waitKey(0)
# 0 means infinite
# cv2.destroyWindow()
# if waitKey(1000) then 1 sec.


if k==10:
    cv2.destroyWindows()
elif k==ord('s'):
    cv2.imwrite('img1_copy.png', img)
