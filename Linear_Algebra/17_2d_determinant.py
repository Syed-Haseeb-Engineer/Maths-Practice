import numpy as np
import matplotlib.pyplot as plt

M = np.array([[3, 0], [1, 2]]) # Det should be (3*2)-(0*1) = 6
sq = np.array([[0, 1, 1, 0, 0], [0, 0, 1, 1, 0]])
transformed = np.dot(M, sq)

det = np.linalg.det(M)
print(f"Original Area: 1x1 = 1")
print(f"Determinant: {det:.1f}")
print("The new shape fits exactly 6 unit squares inside it!")

plt.figure(figsize=(5,5))
plt.fill(sq[0], sq[1], 'blue', alpha=0.3, label='Original Area=1')
plt.fill(transformed[0], transformed[1], 'red', alpha=0.3, label=f'New Area={det:.1f}')
plt.grid(True); plt.legend(); plt.xlim(0, 4); plt.ylim(0, 4)
plt.title("18. Determinant (Area Scaling)")
plt.show()