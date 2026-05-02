import numpy as np
import matplotlib.pyplot as plt

# Data
single_vector = np.array([3, 4])
multiple_vectors = np.random.randn(100, 2) * 2 # 100 vectors (Dataset)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# Plot 1: Single Vector -> Arrow
ax1.quiver(0, 0, single_vector[0], single_vector[1], angles='xy', scale_units='xy', scale=1, color='blue')
ax1.set_title("Single Vector (Arrow)")
ax1.set_xlim(-1, 5); ax1.set_ylim(-1, 5); ax1.grid(True)

# Plot 2: Multiple Vectors -> Points
ax2.scatter(multiple_vectors[:, 0], multiple_vectors[:, 1], c='purple', alpha=0.6)
ax2.set_title("Multiple Vectors (Points / Scatter)")
ax2.set_xlim(-5, 5); ax2.set_ylim(-5, 5); ax2.grid(True)

plt.show()
