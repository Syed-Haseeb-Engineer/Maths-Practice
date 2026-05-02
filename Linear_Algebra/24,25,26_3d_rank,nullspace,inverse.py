import numpy as np
import matplotlib.pyplot as plt

# A matrix where the 3rd column is exactly the 1st column
M_3d = np.array([
    [1, 2, 1],
    [3, 4, 3],
    [5, 6, 5]
])

print("--- 3D Matrix Properties ---")
print(M_3d)
print(f"Rank (26): {np.linalg.matrix_rank(M_3d)} (Spans a 2D plane in 3D space)")

# Null Space (27): Vector [-1, 0, 1] cancels out Col 1 and Col 3
null_v = np.array([-1, 0, 1])
print(f"Null Vector check: M * [-1, 0, 1] = {np.dot(M_3d, null_v)} (Null space exists!)")

# --- VISUALIZATION ADDED BELOW ---
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# 1. Plot the Column Space (Spans a 2D Plane)
c1, c2 = M_3d[:, 0], M_3d[:, 1]
ax.quiver(0, 0, 0, c1[0], c1[1], c1[2], color='blue', label='Col 1 & 3')
ax.quiver(0, 0, 0, c2[0], c2[1], c2[2], color='cyan', label='Col 2')

# Create a visual plane using the two independent columns
grid = np.linspace(-2, 2, 5)
c1_grid, c2_grid = np.meshgrid(grid, grid)
plane_x = c1[0]*c1_grid + c2[0]*c2_grid
plane_y = c1[1]*c1_grid + c2[1]*c2_grid
plane_z = c1[2]*c1_grid + c2[2]*c2_grid
ax.plot_surface(plane_x, plane_y, plane_z, color='blue', alpha=0.2)

# 2. Plot the Null Vector
ax.quiver(0, 0, 0, null_v[0], null_v[1], null_v[2], color='red', label='Null Vector [-1,0,1]')
# Plot where the Null Vector goes (The Origin)
ax.scatter(0, 0, 0, color='black', s=100, label='Origin (Where Null Vec lands)')

ax.set_title("Rank 2 Matrix: Col Space is a Plane, Null Vec maps to Origin")
ax.set_xlim(-6, 6); ax.set_ylim(-6, 6); ax.set_zlim(-6, 6)
ax.legend()
plt.show()