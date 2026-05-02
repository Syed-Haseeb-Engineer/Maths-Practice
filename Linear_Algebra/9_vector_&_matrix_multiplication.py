import numpy as np
import matplotlib.pyplot as plt

# The Matrix
M = np.array([[1, 2], 
              [2, 4]])

# The Vector (Let's pick x=1, y=2)
v = np.array([1, 2])

# Multiply
v_transformed = np.dot(M, v)

print("Matrix M:")
print(M)
print(f"Original Vector v: {v}")
print(f"Transformed Vector: {v_transformed}")

plt.figure(figsize=(6, 6))
# Plot original
plt.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='blue', label='Original v [1,2]')
# Plot transformed
plt.quiver(0, 0, v_transformed[0], v_transformed[1], angles='xy', scale_units='xy', scale=1, color='red', label='Transformed v [5,10]')

plt.xlim(-1, 6)
plt.ylim(-1, 11)
plt.grid(True, linestyle='--')
plt.legend()
plt.title("10. Matrix [1 2; 2 4] applied to Vector")
plt.show()