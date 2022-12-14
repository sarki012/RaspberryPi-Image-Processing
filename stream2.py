import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 5)
if cap.isOpened():
    print("Video Capture Opened")

x = 0
while True:
    try:
        ret, frame = cap.read()
        #print(ret)
        if ret != False and x != 0:
            cv2.imshow('Image',frame)
            cv2.waitKey(1)
        x = 1

    except KeyboardInterrupt:
        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()
        raise SystemExit