# Dependencies
from random import random

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import sem


# "Will you vote for a republican in this election?"
sample_size = 100
samples = [[True if random() < 0.5 else False for x in range(0, sample_size)]
           for y in range(0, 10)]
x_axis = np.arange(0, len(samples), 1)

means = [np.mean(s) for s in samples]
standard_errors = [sem(s) for s in samples]

# Setting up the plot
fig, ax = plt.subplots()

ax.errorbar(x_axis, means, standard_errors, fmt="o")

ax.set_xlim(-1, len(samples) + 1)

ax.set_xlabel("Sample Number")
ax.set_ylabel("Proportion of People Voting Republican")

plt.show()
