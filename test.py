
import numpy as np
import matplotlib.pyplot as plt
from eulerspiral import eulerspiral


hdg = 0 * np.pi / 180

x0 = 0
y0 = 0

fig, axs = plt.subplots(1, 2)

for ax, length in zip(axs, [5, 10]):
    s = np.linspace(0, length, 20)

    for curvStart in [-0.5, -0.1, 0.0, 0.1, 0.5]:
        for curvEnd in [-0.5, -0.1, 0.0, 0.1, 0.5]:

            spiral = eulerspiral.EulerSpiral.createFromLengthAndCurvature(length, curvStart, curvEnd)
            (x, y, t) = spiral.calc(s, x0, y0, curvStart, hdg)

            ax.plot(x, y, marker="x", linewidth=0.5)
            ax.grid(True)
            ax.set_xlim(-5, 11)
            ax.set_ylim(-10, 10)
            ax.set_aspect('equal', 'datalim')
            ax.set_title('length = {}'.format(length))

plt.show()
