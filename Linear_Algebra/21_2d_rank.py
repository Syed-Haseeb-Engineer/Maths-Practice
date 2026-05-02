import numpy as np
import matplotlib.pyplot as plt

M_ind = np.array([[1, 2], [3, 4]])
M_dep = np.array([[1, 2], [2, 4]]) # Row 2 is 2x Row 1

print("--- Rank in 2D ---")
print(f"Independent Matrix Rank: {np.linalg.matrix_rank(M_ind)} (Full Rank, spans 2D)")
print(f"Dependent Matrix Rank: {np.linalg.matrix_rank(M_dep)} (Deficient Rank, spans 1D)")

# --- VISUALIZATION ADDED BELOW ---
# Create a circular cloud of 300 random points (representing 2D space)
points = np.random.randn(2, 300)

# Apply both matrices
ind_transformed = np.dot(M_ind, points)
dep_transformed = np.dot(M_dep, points)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# Plot Independent (Maintains 2D Area)
ax1.scatter(ind_transformed[0], ind_transformed[1], c='green', s=10, alpha=0.6)
ax1.set_title("Independent: Preserves 2D Space (Rank 2)")
ax1.grid(True); ax1.axhline(0, color='k'); ax1.axvline(0, color='k')
ax1.set_xlim(-15, 15); ax1.set_ylim(-15, 15)

# Plot Dependent (Collapses to 1D Line)
ax2.scatter(dep_transformed[0], dep_transformed[1], c='red', s=10, alpha=0.6)
ax2.set_title("Dependent: Collapses to 1D Line (Rank 1)")
ax2.grid(True); ax2.axhline(0, color='k'); ax2.axvline(0, color='k')
ax2.set_xlim(-15, 15); ax2.set_ylim(-15, 15)

plt.show()