import numpy as np
import matplotlib.pyplot as plt

# A 3x2 "Tall" Matrix. 
# It takes a 2D input [x, y] and outputs a 3D vector [x, y, z]
# In this case, z will be a combination of x and y (x + y)
M_tall = np.array([
    [1, 0],  # X output
    [0, 1],  # Y output
    [1, 1]   # Z output
])

print(f"Matrix Shape: {M_tall.shape} (3 Rows = 3D Output, 2 Columns = 2D Input)")

# Create a 2D Grid (Input Space)
x, y = np.meshgrid(np.linspace(-2, 2, 5), np.linspace(-2, 2, 5))
grid_2d = np.vstack([x.flatten(), y.flatten()]) # Shape: (2, 25)

# Multiply! This maps the 2D points into 3D space.
# (3x2) dot (2x25) = (3x25)
grid_3d = np.dot(M_tall, grid_2d)

fig = plt.figure(figsize=(12, 5))

# Plot 1: The Original 2D Input Space
ax1 = fig.add_subplot(121)
ax1.scatter(grid_2d[0], grid_2d[1], color='blue', s=40)
ax1.set_title("Input: 2D Space")
ax1.set_xlim(-3, 3); ax1.set_ylim(-3, 3)
ax1.grid(True); ax1.axhline(0, color='black'); ax1.axvline(0, color='black')

# Plot 2: The Transformed 3D Output Space
ax2 = fig.add_subplot(122, projection='3d')
ax2.scatter(grid_3d[0], grid_3d[1], grid_3d[2], color='red', s=40)
ax2.set_title("Output: Embedded into 3D Space")

# Set 3D limits to see the tilt clearly
ax2.set_xlim(-3, 3); ax2.set_ylim(-3, 3); ax2.set_zlim(-5, 5)

plt.show()

print("Notice that the result is a flat 2D plane, but it now 'lives' inside a 3D world!")
print("Because it's flat, it has no 3D Volume. If we tried to take a 3D determinant, it wouldn't work.")

