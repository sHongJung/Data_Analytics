# Dependencies
from matplotlib import pyplot as plt
from scipy.stats import linregress

import numpy as np


x_axis = np.arange(0, 10, 1)
fake = [1, 2.5, 2.75, 4.25, 5.5, 6, 7.25, 8, 8.75, 9.8]

(slope, intercept, _, _, _) = linregress(x_axis, fake)
fit = slope * x_axis + intercept

fig, ax = plt.subplots()

fig.suptitle("Fake Banana Data!", fontsize=16, fontweight="bold")

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

ax.set_xlabel("Fake Banana Ages (in days)")
ax.set_ylabel("Fake Banana Weights (in Hundres of Kilograms)")

ax.plot(x_axis, fake, linewidth=0, marker='o')
ax.plot(x_axis, fit, 'b--')

plt.show()
