import numpy as np
import matplotlib.pyplot as plt

# Eq 1: 2x + y = 5  => y = 5 - 2x
# Eq 2: 4x + 2y = 4 => 2y = 4 - 4x => y = 2 - 2x
x_vals = np.linspace(0, 4, 100)
y1 = 5 - 2*x_vals
y2 = 2 - 2*x_vals

A = np.array([[2, 1], [4, 2]])
det = np.linalg.det(A)

print(f"Determinant: {det:.1f}. Because it's 0, no unique solution exists.")

plt.figure(figsize=(5,5))
plt.plot(x_vals, y1, '-b', label='2x + y = 5')
plt.plot(x_vals, y2, '-r', label='4x + 2y = 4')

plt.grid(True); plt.legend(); plt.ylim(0, 6)
plt.title(f"29. Dependent Lines (Det = {det:.1f}) = Parallel")
plt.show()