import numpy as np
import matplotlib.pyplot as plt

im_uint8 = np.random.randint(0, 256, (200, 200, 3), dtype=np.uint8)
im_fl32 = np.random.rand(200, 200, 3).astype(np.float32)
im_fl64 = np.random.rand(200, 200, 3)
plt.subplot(1, 3, 1)
plt.imshow(im_uint8)
plt.subplot(1, 3, 2)
plt.imshow(im_fl32)
plt.subplot(1, 3, 3)
plt.imshow(im_fl64)
plt.show()