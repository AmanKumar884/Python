# 6(camera video capturing)
import cv2
cap=cv2.VideoCapture(0)

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

cap.set(3, 1200)  # width
cap.set(4, 720)  # height

print(cap.get(3))
print(cap.get(4))


while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', frame)

        # frame replaced by gray

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()

cv2.destroyAllWindows()