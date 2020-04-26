"""Gráfica de aproximación de pi con simulación
monte carlo"""

import matplotlib.pyplot as plt
import numpy as np
from math import tau

plt.style.use("dark_background")

theta = np.linspace(0, tau / 4, num=1000)
circle_x = np.cos(theta)
circle_y = np.sin(theta)

n = 10_000
x = np.random.random(n)
y = np.random.random(n)

fig, ax = plt.subplots(figsize=(10, 10), dpi=128)
ax.plot(circle_x, circle_y, linewidth=3)
ax.scatter(
    x, y, s=5, edgecolors=None, c=abs(x + y), cmap=plt.cm.viridis,
)
ax.set_xlim([-0.01, 1.01])
ax.set_ylim([-0.01, 1.01])
ax.tick_params(axis="both", labelsize=14)
ax.yscale = False
ax.xscale = False
ax.set_xlabel("$x$", fontsize=24)
ax.set_ylabel("$y$", fontsize=24)
ax.set_xticks([0, 1])
ax.set_yticks([0, 1])
ax.grid()
plt.savefig("./img/montecarlo.png", bbox_inches="tight")
# plt.show()
