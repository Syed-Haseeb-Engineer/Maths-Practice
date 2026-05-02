import numpy as np
import matplotlib.pyplot as plt

# Eq 1: x + y + z = 3     => z = 3 - x - y
# Eq 2: x - y + 2z = 4    => z = (4 - x + y) / 2
# Eq 3: 2x + y - z = 1    => z = 2x + y - 1

A = np.array([
    [1,  1,  1],
    [1, -1,  2],
    [2,  1, -1]
])
b = np.array([3, 4, 1])

det = np.linalg.det(A)
print(f"Determinant of A: {det:.2f}")

# Calculate the exact intersection point!
solution = np.linalg.solve(A, b)
print(f"The Unique Solution Point is: x={solution[0]}, y={solution[1]}, z={solution[2]}")

x, y = np.meshgrid(np.linspace(-2, 4, 10), np.linspace(-2, 4, 10))

z1 = 3 - x - y
z2 = (4 - x + y) / 2
z3 = 2*x + y - 1

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(x, y, z1, alpha=0.4, color='blue')
ax.plot_surface(x, y, z2, alpha=0.4, color='green')
ax.plot_surface(x, y, z3, alpha=0.4, color='yellow')

# Plot the exact solution point where they all cross
ax.scatter(solution[0], solution[1], solution[2], color='red', s=200, label='Solution Point')

ax.set_title(f"32. Independent System (Det = {det:.1f}) \nPlanes intersect at exactly one point!")
ax.legend()
plt.show()