import numpy as np
import matplotlib.pyplot as plt


def create_complex_matrix(x1, x2, y1, y2, quality):
    x = np.linspace(x1, x2, int((x2 - x1) * quality))
    y = np.linspace(y1, y2, int((y2 - y1) * quality))
    return x[np.newaxis, :] + y[:, np.newaxis] * 1j

def julia(c, i):
    z = c
    z_list = []
    for _ in range(i):
        z = z ** 2 + c
        z_list.append(z)
    return z_list

plan = create_complex_matrix(-2, 0.5, -1.5, 1.5, quality=1000)
mask = julia(complex(-0.1, 0.651), i=30)

plt.imshow(mask, cmap="binary")
plt.show()