import numpy as np
import matplotlib.pyplot as plt

M = np.array([[1, 2], [2, 4]]) # Dependent matrix
# Null space vector (x = -2y)
null_v = np.array([-2, 1])

# Apply matrix to null vector
result = np.dot(M, null_v)

print(f"Matrix M applied to Null Vector {null_v} = {result}")

plt.figure(figsize=(5,5))
plt.quiver(0, 0, null_v[0], null_v[1], angles='xy', scale_units='xy', scale=1, color='g', label='Null Vector [-2, 1]')
plt.plot(result[0], result[1], 'ro', markersize=10, label='Transformed to Origin [0,0]')
plt.xlim(-3, 3); plt.ylim(-2, 3); plt.grid(True); plt.legend()
plt.title("23. Null Space (Mapped to Origin)")
plt.show()