import cv2
import numpy as np
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
prev = None
frame2 = None
iframe = 0
while True:
    iframe += 1
    _, frame = cap.read()
    frame2 = frame.copy()
    if prev is not None:
        diff = cv2.absdiff(prev, frame)
        d = diff.sum()
        print(d)
        if d > 4e6:
            frame2[:, :, :2] = 0
        cv2.imshow('diff', diff)
    prev = frame.copy()
    if frame2 is not None:
        cv2.imshow('frame', frame2)
    cv2.waitKey(1)