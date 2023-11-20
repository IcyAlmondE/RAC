import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
bg = None
iframe = 0
while True:
    iframe+=1
    _, frame = cap.read()
    if iframe ==15:
        bg = frame.copy()
    if iframe >15:
        diff = cv2.absdiff(bg, frame)
        d=diff.sum()
        if d>2e7:
            frame[:, :, :2]=0
        cv2.imshow('diff', diff)

    cv2.imshow('frame', frame)
    cv2.waitKey(1)