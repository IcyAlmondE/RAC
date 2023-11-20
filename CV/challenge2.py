import numpy as np
import cv2
import matplotlib.pyplot as plt

def image2bitplane(img):
    bp = []
    for c in range(img.shape[2]):
        for i in range(8):
            bp.append(img[:, :, c] // 2 ** i % 2)
    return np.array(bp)


def bitplane2image(bp):
    img = np.zeros((bp[0].shape[0], bp[0].shape[1], 3))
    for b in range(len(bp)):
        img[:, :, b//8] = img[:, :, b//8] + (bp[b] * 2**(b % 8))
    return np.uint8(img)

image = cv2.imread('challenge_2.png')[:, :, ::-1]
imbp = image2bitplane(image)
idx_ans = np.r_[0:4, 8:12, 16:20][::-1]
idx = np.r_[4:8, 12:16, 20:24]

bp_ans = np.zeros_like(imbp)
bp_ans[idx] = imbp[idx_ans]
ans = bitplane2image(bp_ans)

plt.imshow(ans)
plt.show()