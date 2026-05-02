import numpy as np
import matplotlib.pyplot as plt

# Generating points (combinations) to see the reachable space
scalars = np.linspace(-2, 2, 20)
c1, c2 = np.meshgrid(scalars, scalars)

# --- INDEPENDENT --- (They point different ways)
v1_ind = np.array([1, 0])
v2_ind = np.array([0, 1])
points_ind = (c1[..., np.newaxis] * v1_ind) + (c2[..., np.newaxis] * v2_ind)
points_ind = points_ind.reshape(-1, 2)

# --- DEPENDENT --- (v2 is just v1 multiplied by 2)
v1_dep = np.array([1, 1])
v2_dep = np.array([2, 2])
points_dep = (c1[..., np.newaxis] * v1_dep) + (c2[..., np.newaxis] * v2_dep)
points_dep = points_dep.reshape(-1, 2)

print(f"Independent Rank: {np.linalg.matrix_rank(np.column_stack((v1_ind, v2_ind)))}")
print(f"Dependent Rank: {np.linalg.matrix_rank(np.column_stack((v1_dep, v2_dep)))}")

# Visualization
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Independent plot (Creates a 2D plane of points)
ax1.scatter(points_ind[:, 0], points_ind[:, 1], c='green', s=5)
ax1.set_title("Independent (Spans a 2D Plane)")
ax1.grid(True); ax1.set_xlim(-4, 4); ax1.set_ylim(-4, 4)

# Dependent plot (Trapped on a 1D line)
ax2.scatter(points_dep[:, 0], points_dep[:, 1], c='red', s=5)
ax2.set_title("Dependent (Trapped on a 1D Line)")
ax2.grid(True); ax2.set_xlim(-6, 6); ax2.set_ylim(-6, 6)

plt.show()