import numpy as np
import matplotlib.pyplot as plt

# The operation
v = np.array([2, 1.5])
scalar = 2.5
v_scaled = v * scalar

print(f"Original v: {v}")
print(f"Scaled by {scalar}: {v_scaled}")

# The visualization
plt.figure(figsize=(6, 6))
# Plot the scaled vector first (so it sits behind the original)
plt.quiver(0, 0, v_scaled[0], v_scaled[1], angles='xy', scale_units='xy', scale=1, color='red', label='Scaled Vector')
# Plot original vector
plt.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='blue', label='Original Vector')

plt.xlim(0, 6)
plt.ylim(0, 5)
plt.grid(True, linestyle='--')
plt.legend()
plt.title(f"4. Vector Scaled by {scalar}")
plt.show()