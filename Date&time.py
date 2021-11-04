import numpy as np
import cv2
import datetime
cap=cv2.VideoCapture(0)

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# cap.set(3, 1200)  # width
# cap.set(4, 720)  # height

# print(cap.get(3))
# print(cap.get(4))


while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("SORRY NOT OPENING")
        break

    font=cv2.FONT_HERSHEY_SIMPLEX
    text = 'Width: '+ str(cap.get(2)) + '  Height: '+str(cap.get(4))

    datet = str(datetime.datetime.now())
    frame = cv2.putText(frame, datet, (10, 50), font, 1, (0, 255, 255), 2, cv2.LINE_AA)
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', frame)

    # frame replaced by gray

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()