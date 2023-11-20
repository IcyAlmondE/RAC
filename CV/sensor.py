import cv2
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
prev = None
frame2 = None
frame3 = None
iframe = 0
L = 100
L2 = 500
while True:
    iframe += 1
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame2 = frame.copy()
    if prev is not None:
        diff1 = cv2.absdiff(prev[:, L:L+10], frame[:, L:L+10])
        d1 = diff1.sum()

        diff2 = cv2.absdiff(prev[:, L2:L2 + 10], frame[:, L2:L2 + 10])
        d2 = diff2.sum()

        print(d1)
        if d1 > 1e5:
            frame2[:, L:L+10, :2] = 0
        else:
            frame2[:, L:L + 10, [0, 2]] = 0

        if d2 > 1e5:
            frame2[:, L2:L2 + 10, :2] = 0
        else:
            frame2[:, L2:L2 + 10, [0, 2]] = 0
        cv2.imshow('diff', diff1)
        cv2.imshow('diff', diff2)
    prev = frame.copy()
    if frame2 is not None:
        cv2.imshow('frame', frame2)
    cv2.waitKey(1)