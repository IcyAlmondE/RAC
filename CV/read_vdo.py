import cv2

cap = cv2.VideoCapture('vdo.mp4')
while True:
    _, frame = cap.read()
    cv2.imshow('frame', frame)
    cv2.waitKey(1)