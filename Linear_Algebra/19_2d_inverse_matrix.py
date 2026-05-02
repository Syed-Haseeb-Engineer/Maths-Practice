import numpy as np
import matplotlib.pyplot as plt

M = np.array([[2, 1], [1, 2]])
M_inv = np.linalg.inv(M)

sq = np.array([[0, 1, 1, 0, 0], [0, 0, 1, 1, 0]])

# Forward transform
step1 = np.dot(M, sq)
# Reverse transform
step2 = np.dot(M_inv, step1)

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12, 4))
ax1.plot(sq[0], sq[1], 'b-o'); ax1.set_title("1. Original"); ax1.grid(True)
ax2.plot(step1[0], step1[1], 'r-o'); ax2.set_title("2. Transformed (M)"); ax2.grid(True)
ax3.plot(step2[0], step2[1], 'g-o'); ax3.set_title("3. Restored (M_inv)"); ax3.grid(True)
plt.show()
