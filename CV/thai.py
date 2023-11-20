import numpy as np
import matplotlib.pyplot as plt

thai = np.ones((6, 8, 3))
thai[[0, -1], :, 1:]=0
thai[2:4, :, :2]=0

plt.imshow(thai)
plt.show()