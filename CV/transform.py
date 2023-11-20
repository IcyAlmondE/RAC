import cv2
import numpy as np
from skimage.measure import label, regionprops

def onClick(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print([x, y])
        if len(pts1) < 4:
            pts1.append([x, y])

pts1=[]
pts2=[(0, 0), (750, 0), (750, 525), (0, 525)]

T = None
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cv2.namedWindow('frame')
cv2.setMouseCallback('frame', onClick)
while True:
    _, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    bw = cv2.threshold(gray, 125, 255, cv2.THRESH_BINARY)[1]
    if len(pts1) == 4:
        T = cv2.getPerspectiveTransform(np.float32(pts1), np.float32(pts2))
    if T is not None:
        frame = cv2.warpPerspective(frame, T, (750, 525))
        bw = 255-cv2.warpPerspective(bw, T, (750, 525))
        bw = cv2.erode(bw, np.ones((11, 11)))
        Label = label(bw.astype(float)/255)
        print(len(np.unique(Label)-1))

        for r in regionprops(Label):
            print(r.label, r.area)

    cv2.imshow('frame', frame)
    cv2.imshow('bw', bw)
    cv2.waitKey(1)