import numpy as np
import matplotlib.pyplot as plt


def create_complex_matrix(x1, x2, y1, y2, quality):
    x = np.linspace(x1, x2, int((x2 - x1) * quality))
    y = np.linspace(y1, y2, int((y2 - y1) * quality))
    return x[np.newaxis, :] + y[:, np.newaxis] * 1j

@np.vectorize
def julia(z0, c, i):
    z = z0
    for it in range(i):
        z = z ** 2 + c
        if abs(z) > 2: break
    return it

plan = create_complex_matrix(-8, 2, -6, 6, quality=1000)
julia = julia(plan, complex(-0.4, 0.6), i=50)

plt.imshow(julia, cmap="viridis")
plt.show()
