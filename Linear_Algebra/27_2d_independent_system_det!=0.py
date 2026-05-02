import numpy as np
import matplotlib.pyplot as plt

# Eq 1: 2x + y = 5  => y = 5 - 2x
# Eq 2: x - y = 1   => y = x - 1
x_vals = np.linspace(0, 4, 100)
y1 = 5 - 2*x_vals
y2 = x_vals - 1

A = np.array([[2, 1], [1, -1]])
b = np.array([5, 1])
det = np.linalg.det(A)

# Calculate exact intersection
solution = np.linalg.solve(A, b)

plt.figure(figsize=(5,5))
plt.plot(x_vals, y1, '-b', label='2x + y = 5')
plt.plot(x_vals, y2, '-r', label='x - y = 1')
plt.plot(solution[0], solution[1], 'go', markersize=8, label=f'Solution {solution}')

plt.grid(True); plt.legend()
plt.title(f"30. Independent Lines (Det = {det:.1f})")
plt.show()
