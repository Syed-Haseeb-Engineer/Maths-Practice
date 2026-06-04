# 32. Dot Product and Duality
import numpy as np
import matplotlib.pyplot as plt

# 1. Define the vectors
v = np.array([3, 1])  # The vector that will define our 1D line
w = np.array([1, 2])  # The vector we are going to transform/project

# 2. Method A: Standard Dot Product (The Physics way)
dot_product = np.dot(v, w)

# 3. Method B: Duality / Matrix Multiplication (The Math way)
# We treat 'v' as a 1x2 transformation matrix that crushes 2D space onto a 1D line
matrix_v = np.array([[3, 1]]) # Shape: (1 row, 2 columns)
vector_w = np.array([[1],     # Shape: (2 rows, 1 column)
                     [2]])
transformation_result = matrix_v @ vector_w

# 4. Geometrically: Projection (The Visual way)
# Formula to find exactly where the shadow lands: (v • w / ||v||^2) * v
v_mag_sq = np.dot(v, v)
proj_w_on_v = (dot_product / v_mag_sq) * v

print("--- Chapter 9: Duality ---")
print(f"Vector v: {v}")
print(f"Vector w: {w}\n")
print(f"Method A (Dot Product): v • w = {dot_product}")
print(f"Method B (1x2 Matrix): [3 1] @ [1; 2] = {transformation_result[0][0]}")
print("Notice they are exactly the same mathematical operation!")

# --- VISUALIZATION ---
fig, ax = plt.subplots(figsize=(8, 6))

# Draw the infinite line spanned by v (This is the 1D space everything collapses onto)
x_vals = np.linspace(-2, 4, 100)
y_vals = (v[1]/v[0]) * x_vals
ax.plot(x_vals, y_vals, 'k--', alpha=0.4, label='1D Number Line (Span of v)')

# Draw the original vectors
ax.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='blue', label='Vector v [3,1]')
ax.quiver(0, 0, w[0], w[1], angles='xy', scale_units='xy', scale=1, color='red', label='Vector w [1,2]')

# Draw the projection (The shadow of w landing on v)
ax.quiver(0, 0, proj_w_on_v[0], proj_w_on_v[1], angles='xy', scale_units='xy', scale=1, color='green', lw=4, alpha=0.7, label='Projection of w onto v')

# Draw the dashed line showing the 'shadow' dropping straight down at a perfect 90-degree angle
ax.plot([w[0], proj_w_on_v[0]], [w[1], proj_w_on_v[1]], 'k:', lw=2, label='Projection path (90° Angle)')

ax.set_xlim(-1, 4)
ax.set_ylim(-1, 3)
ax.axhline(0, color='black', lw=0.5)
ax.axvline(0, color='black', lw=0.5)
ax.grid(True)
ax.set_title(f"Duality: Dot Product (Projection) = Matrix Transformation = {dot_product}")
ax.legend()
plt.show()