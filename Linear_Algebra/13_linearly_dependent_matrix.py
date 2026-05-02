import numpy as np
import matplotlib.pyplot as plt

# Dependent matrix (Row 2 is just Row 1 multiplied by -1)
M_dep = np.array([[ 1,  2], 
                  [-1, -2]])

print(f"Determinant: {np.linalg.det(M_dep)}")

# Create a cloud of 100 random 2D points (A 2D plane of data)
points = np.random.uniform(-5, 5, (2, 100))

# Apply the dependent matrix
collapsed_points = np.dot(M_dep, points)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Original 2D Cloud
ax1.scatter(points[0], points[1], color='blue', s=10)
ax1.set_title("Original Data (2D Plane)")
ax1.set_xlim(-15, 15); ax1.set_ylim(-15, 15)
ax1.grid(True); ax1.axhline(0, color='black'); ax1.axvline(0, color='black')

# Transformed Cloud (Collapsed!)
ax2.scatter(collapsed_points[0], collapsed_points[1], color='red', s=10)
ax2.set_title("Transformed Data (Collapsed to 1D Line)")
ax2.set_xlim(-15, 15); ax2.set_ylim(-15, 15)
ax2.grid(True); ax2.axhline(0, color='black'); ax2.axvline(0, color='black')

plt.show()
