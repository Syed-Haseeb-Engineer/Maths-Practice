import numpy as np
import matplotlib.pyplot as plt

# 90 Degree Counter-Clockwise Matrix
Rot90 = np.array([[0, -1], 
                  [1,  0]])

# Original vector
v = np.array([3, 1])

# Apply rotation
v_rot = np.dot(Rot90, v)

plt.figure(figsize=(6, 6))
plt.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='blue', label='Original Vector')
plt.quiver(0, 0, v_rot[0], v_rot[1], angles='xy', scale_units='xy', scale=1, color='green', label='Rotated 90°')

# Draw a right angle square to prove it's 90 degrees
plt.plot([0, -0.5, -0.3, 0.2], [0, 1.5, 1.9, 0.4], 'k-', alpha=0.0) # Hidden anchor
plt.gca().add_patch(plt.Rectangle((0,0), 0.5, 0.5, angle=np.degrees(np.arctan2(v[1], v[0])), fill=False, color='red'))

plt.xlim(-4, 4)
plt.ylim(-1, 4)
plt.grid(True, linestyle='--')
plt.axhline(0, color='black'); plt.axvline(0, color='black')
plt.legend()
plt.title("12. 90 Degree Rotation")
plt.show()