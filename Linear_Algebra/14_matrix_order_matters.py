import numpy as np
import matplotlib.pyplot as plt

# Matrices
Rot90 = np.array([[0, -1], [1, 0]])
Shear = np.array([[1, 1], [0, 1]])

# Square
sq = np.array([[0, 1, 1, 0, 0], [0, 0, 1, 1, 0]])

# 1. Rotate THEN Shear (Shear * Rot * sq)
rot_first = np.dot(Rot90, sq)
rot_then_shear = np.dot(Shear, rot_first)

# 2. Shear THEN Rotate (Rot * Shear * sq)
shear_first = np.dot(Shear, sq)
shear_then_rot = np.dot(Rot90, shear_first)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
ax1.plot(rot_then_shear[0], rot_then_shear[1], 'r-o')
ax1.set_title("1. Rotate -> 2. Shear")
ax1.grid(True); ax1.set_xlim(-3, 3); ax1.set_ylim(-1, 3)

ax2.plot(shear_then_rot[0], shear_then_rot[1], 'b-o')
ax2.set_title("1. Shear -> 2. Rotate")
ax2.grid(True); ax2.set_xlim(-3, 3); ax2.set_ylim(-1, 3)
plt.show()

print("Notice the shapes end up in completely different locations and orientations!")