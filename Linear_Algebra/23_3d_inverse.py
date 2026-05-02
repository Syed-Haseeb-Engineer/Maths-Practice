import numpy as np
import matplotlib.pyplot as plt

M = np.array([[1, 0, 2], [0, 1, 0], [3, 0, 1]])
v = np.array([5, 5, 5])

M_inv = np.linalg.inv(M)
v_transformed = np.dot(M, v)
v_restored = np.dot(M_inv, v_transformed)

print("--- 3D Inverse ---")
print(f"Original v: {v}")
print(f"Transformed: {v_transformed}")
print(f"Restored via Inverse: {np.round(v_restored, 1)}")

# --- VISUALIZATION ADDED BELOW ---
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Draw arrows for the vectors
ax.quiver(0, 0, 0, v[0], v[1], v[2], color='blue', lw=3, label='1. Original Vector')
ax.quiver(0, 0, 0, v_transformed[0], v_transformed[1], v_transformed[2], color='red', lw=2, label='2. Transformed (M)')
ax.quiver(0, 0, 0, v_restored[0], v_restored[1], v_restored[2], color='green', lw=5, alpha=0.5, label='3. Restored (M_inv)')

ax.set_title("3D Inverse: Green perfectly overlays Blue")
ax.set_xlim(0, 16); ax.set_ylim(0, 16); ax.set_zlim(0, 20)
ax.legend()
plt.show()