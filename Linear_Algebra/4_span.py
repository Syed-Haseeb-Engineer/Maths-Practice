import numpy as np
import matplotlib.pyplot as plt

# The operations

#Linearly dependend means if we multiple any constant with different vectors they will on same line
# v1 = np.array([1, 0.5])
# v2 = np.array([-1, -0.5])

#Linearly independent means if we multiple any constant with different vectors they will not on same line
v1 = np.array([1, 0.5])
v2 = np.array([-0.5, 1])


print(f"Spanning space using base vectors {v1} and {v2}...")

# Generate 500 random linear combinations (c1*v1 + c2*v2)
c1 = np.random.uniform(-3, 3, 500)
c2 = np.random.uniform(-3, 3, 500)

# Multiply combinations (Multiple vectors = points)
span_points = np.outer(c1, v1) + np.outer(c2, v2)

# Visualization
plt.figure(figsize=(6, 6))
# Plot the multiple vectors as points
plt.scatter(span_points[:, 0], span_points[:, 1], color='purple', s=5, alpha=0.5, label='Span (Combinations)')
# Plot the original two base vectors as arrows
plt.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='blue', label='v1')
plt.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='red', label='v2')

plt.xlim(-4, 4)
plt.ylim(-4, 4)
plt.grid(True, linestyle='--')
plt.axhline(0, color='black', lw=1); plt.axvline(0, color='black', lw=1)
plt.legend()
plt.title("5. Span (All possible linear combinations)")
plt.show()