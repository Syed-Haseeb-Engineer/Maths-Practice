import numpy as np
import matplotlib.pyplot as plt

# 1. Define two vectors in the XY plane
v = np.array([3, 0, 0])
w = np.array([0, 2, 0])

# 2. Calculate the Cross Product
cross_result = np.cross(v, w)

# 3. Calculate the Area (Length of the cross product vector)
area = np.linalg.norm(cross_result)

print("--- Chapter 10: Cross Product ---")
print(f"Vector v: {v}")
print(f"Vector w: {w}")
print(f"Cross Product (v x w): {cross_result}")
print(f"Area of the Parallelogram: {area}")

# --- VISUALIZATION ---
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot original vectors
ax.quiver(0, 0, 0, v[0], v[1], v[2], color='blue', lw=3, label='Vector v')
ax.quiver(0, 0, 0, w[0], w[1], w[2], color='red', lw=3, label='Vector w')

# Plot the Cross Product Vector
ax.quiver(0, 0, 0, cross_result[0], cross_result[1], cross_result[2], color='green', lw=4, label='Cross Product (v x w)')

# Draw the Parallelogram on the floor
ax.plot([v[0], v[0]+w[0]], [v[1], v[1]+w[1]], [v[2], v[2]+w[2]], 'k--')
ax.plot([w[0], v[0]+w[0]], [w[1], v[1]+w[1]], [w[2], v[2]+w[2]], 'k--')

ax.set_xlim(0, 6); ax.set_ylim(0, 6); ax.set_zlim(0, 8)
ax.set_title(f"Cross Product: Perpendicular Vector with Length = {area}")
ax.legend()
plt.show()