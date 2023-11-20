import numpy as np
import matplotlib.pyplot as plt

jp=np.full((2000, 3000, 3), 255, dtype=np.uint8)

for x in range(len(jp[1])):
    for y in range(len(jp[0])):
        if (x-1500)**2 + (y-1000)**2 <= (600)**2:
            jp[y, x, 0]=188
            jp[y, x, 1] = 0
            jp[y, x, -1] = 45

plt.imshow(jp)
plt.show()