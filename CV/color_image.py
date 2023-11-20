import numpy as np
import matplotlib.pyplot as plt

R = np.zeros((200, 200, 3), dtype=np.uint8)
R[:, :, 0] = 255
G = np.zeros((200, 200, 3), dtype=np.uint8)
G[:, :, 1] = 255
B = np.zeros((200, 200, 3), dtype=np.uint8)
B[:, :, -1] = 255
M = np.zeros((200, 200, 3), dtype=np.uint8)
M[:, :, [0, 2]] = 255
Y = np.zeros((200, 200, 3), dtype=np.uint8)
Y[:, :, [0, 1]] = 255
C = np.zeros((200, 200, 3), dtype=np.uint8)
C[:, :, [1, 2]] = 255
W = np.zeros((200, 200, 3), dtype=np.uint8)
W[:, :, :] = 255
plt.imshow(W)
plt.show()