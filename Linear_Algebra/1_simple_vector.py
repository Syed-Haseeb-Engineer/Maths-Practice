import numpy as np
import matplotlib.pyplot as plt

# The operation: Defining a single vector
v = np.array([3, 4])

print(f"Vector v: {v}")

# The visualization (Single = Arrow)
plt.figure(figsize=(5, 5))
plt.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='blue')

plt.xlim(-1, 5)
plt.ylim(-1, 5)
plt.grid(True, linestyle='--')
plt.axhline(0, color='black', lw=1)
plt.axvline(0, color='black', lw=1)
plt.title("1. Simple Vector")
plt.show()