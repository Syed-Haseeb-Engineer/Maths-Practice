import numpy as np
import matplotlib.pyplot as plt

# Generate a grid of points
x, y = np.meshgrid(np.arange(-3, 4, 1), np.arange(-3, 4, 1))
grid_points = np.vstack([x.flatten(), y.flatten()])

# Define a transformation matrix (a slight stretch and tilt)
M = np.array([[1.5, 0.5], 
              [0.2, 1.2]])

# Apply transformation
transformed_grid = np.dot(M, grid_points)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# Original Grid
ax1.scatter(grid_points[0], grid_points[1], color='blue', s=10)
ax1.plot(0, 0, 'ro', markersize=8) # Mark the Origin
ax1.set_title("Original Grid (Origin is Red)")
ax1.grid(True); ax1.set_xlim(-6, 6); ax1.set_ylim(-6, 6)
ax1.axhline(0, color='black'); ax1.axvline(0, color='black')

# Transformed Grid
ax2.scatter(transformed_grid[0], transformed_grid[1], color='purple', s=10)
ax2.plot(0, 0, 'ro', markersize=8) # Origin stays in place!
ax2.set_title("Transformed (Lines Parallel, Origin Fixed)")
ax2.grid(True); ax2.set_xlim(-6, 6); ax2.set_ylim(-6, 6)
ax2.axhline(0, color='black'); ax2.axvline(0, color='black')

plt.show()