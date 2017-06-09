
import numpy as np
import matplotlib.pyplot as plt
import eulerspiral



hdg = 0 * np.pi / 180

x0 = 0
y0 = 0


for length in [2, 10]:
    s = np.linspace(0, length, 20)

    for curvStart in [-0.5, -0.1, 0.0, 0.1, 0.5]:
        for curvEnd in [-0.5, -0.1, 0.0, 0.1, 0.5]:

            spiral = eulerspiral.EulerSpiral.createFromLengthAndCurvature(length, curvStart, curvEnd)
            (x, y, t) = spiral.calc(s, x0, y0, curvStart, hdg)

            plt.plot(x, y, marker="x", linewidth=0.5)


plt.grid()
plt.axes().set_aspect('equal', 'datalim')
plt.show()
