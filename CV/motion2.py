import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
bg = None
iframe = 0
prev = None

while True:
    iframe += 1
    _, frame = cap.read()
    frame = cv2.flip(frame,1)

    now = frame.copy()

    if prev is not None:
        diff = cv2.absdiff(frame, prev)
        d = diff.sum()
        print(d)
        if d > 34e5:
            frame[:, :, :2] = 0
        cv2.imshow('Diff', diff)

    # if bg is not None:
    # # if iframe > 15:
    #     diff = cv2.absdiff(frame, bg)
    #     d = diff.sum()
    #     print(d)
    #     if d > 12e6:
    #         frame[:, :, :2] = 0
    #     cv2.imshow('Diff', diff)

    prev = now.copy()

    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break