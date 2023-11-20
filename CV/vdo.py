import cv2
import numpy as np

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
frame_size = (540, 960, 3)
vdo_writer = cv2.VideoWriter('vdo.mp4', fourcc, 30, (frame_size[1], frame_size[0]))

for i in range(240):
    frame = np.zeros(frame_size, np.uint8)
    cv2.circle(frame, (4*i, round(4*(9/16)*i)), 50, (255,255,255), -1)
    vdo_writer.write(frame)
vdo_writer.release()