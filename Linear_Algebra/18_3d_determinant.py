import numpy as np
import matplotlib.pyplot as plt

M_3d = np.array([
    [2, 0, 0],
    [0, 2, 0],
    [0, 0, 2]
])
# A 2x2x2 scaling matrix. Volume should increase by 2*2*2 = 8.
det_3d = np.linalg.det(M_3d)

print("--- 3D Determinant ---")
print(M_3d)
print(f"Determinant (Volume multiplier): {det_3d:.1f}")
print("A 1x1x1 unit cube becomes a 2x2x2 cube (Volume = 8).")

# --- VISUALIZATION ADDED BELOW ---
# Create a 1x1x1 unit cube
r = [0, 1]
x, y, z = np.meshgrid(r, r, r)
cube = np.vstack([x.flatten(), y.flatten(), z.flatten()])

# Transform the cube
transformed_cube = np.dot(M_3d, cube)

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Plot Original Cube (Small, Blue)
ax.scatter(cube[0], cube[1], cube[2], color='blue', s=50, label='Original (Vol=1)')
# Plot Transformed Cube (Large, Red)
ax.scatter(transformed_cube[0], transformed_cube[1], transformed_cube[2], color='red', s=100, alpha=0.5, label=f'Transformed (Vol={det_3d:.0f})')

ax.set_title("3D Determinant: Volume Expansion")
ax.set_xlim(0, 3); ax.set_ylim(0, 3); ax.set_zlim(0, 3)
ax.legend()
plt.show()