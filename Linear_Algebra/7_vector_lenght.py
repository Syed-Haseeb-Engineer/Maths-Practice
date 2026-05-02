import numpy as np
import matplotlib.pyplot as plt

# The operation
v = np.array([5, 3]) # x=5, y=3

# The Math: Length = sqrt(x^2 + y^2)
x_squared = v[0]**2
y_squared = v[1]**2
length_manual = np.sqrt(x_squared + y_squared)

# The built-in NumPy way
length_numpy = np.linalg.norm(v)

print(f"Vector Coordinates: x={v[0]}, y={v[1]}")
print(f"Manual Pythagoras: sqrt({x_squared} + {y_squared}) = {length_manual}")
print(f"NumPy norm result: {length_numpy}")

# The visualization (Forming the right triangle)
plt.figure(figsize=(6, 6))

# Main vector
plt.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='blue', label=f'Vector (Len={length_manual})')

# X component (Base)
plt.plot([0, v[0]], [0, 0], 'r--', lw=3, label=f'Base (x={v[0]})')
# Y component (Height)
plt.plot([v[0], v[0]], [0, v[1]], 'g--', lw=3, label=f'Height (y={v[1]})')

plt.xlim(-1, 5)
plt.ylim(-1, 4)
plt.grid(True, linestyle='--')
plt.legend()
plt.title("8. Calculating Vector Length via Pythagoras")
plt.show()