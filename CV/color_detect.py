import numpy as np
import cv2

tol = 30
color = np.array([100, 100, 100]) #BGR

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
canvas = None
while True :
    _, frame = cap.read()
    mask = cv2.inRange(frame, color-tol, color+tol)
    cv2.imshow('frame', frame)
    # cv2.imshow('mask', mask)

    if canvas is not None:
        canvas = np.float32(canvas) + np.float32(mask)
        canvas = np.uint8(canvas >0)*255
        cv2.imshow('canvas', canvas)
    else:
        canvas = mask.copy()
    cv2.waitKey(1)