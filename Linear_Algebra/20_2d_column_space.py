import numpy as np
import matplotlib.pyplot as plt

# Linearly Dependent Matrix (Col 2 is Col 1 * -1)
M = np.array([[1, -1], [2, -2]])

c1, c2 = M[:, 0], M[:, 1]

plt.figure(figsize=(5,5))
plt.quiver(0, 0, c1[0], c1[1], angles='xy', scale_units='xy', scale=1, color='b', label='Col 1')
plt.quiver(0, 0, c2[0], c2[1], angles='xy', scale_units='xy', scale=1, color='r', label='Col 2')
# Plot the 1D span line
plt.plot([-3, 3], [-6, 6], 'k--', alpha=0.5, label='Column Space (1D Line)')

plt.xlim(-4, 4); plt.ylim(-7, 7); plt.grid(True); plt.legend()
plt.title("21. Column Space of a Dependent Matrix")
plt.show()