import numpy
import matplotlib
import skimage
import cv2
import array

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
while True:
    ret, frame = cap.read()
    # frame = cv2.flip(frame, flipCode=0)
    frame = cv2.flip(frame, flipCode=1)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break
