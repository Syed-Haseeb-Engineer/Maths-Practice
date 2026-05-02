import numpy as np
import matplotlib.pyplot as plt

# The operation
v1 = np.array([2, 1])
v2 = np.array([1, 3])
v3 = v1 + v2  # Vector Addition

print(f"v1: {v1}")
print(f"v2: {v2}")
print(f"v1 + v2 = {v3}")

# The visualization
plt.figure(figsize=(5, 5))
# Plot v1
plt.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='blue', label='v1')
# Plot v2 starting from the tip of v1 (head-to-tail addition)
plt.quiver(v1[0], v1[1], v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='red', label='v2')
# Plot the result from origin to the final tip
plt.quiver(0, 0, v3[0], v3[1], angles='xy', scale_units='xy', scale=1, color='green', label='v1+v2')

plt.xlim(0, 4)
plt.ylim(0, 5)
plt.grid(True, linestyle='--')
plt.legend()
plt.title("2. Vector Addition")
plt.show()