import numpy as np
import matplotlib.pyplot as plt

# 1. Define Base Matrices
A = np.array([[0, -1], [1, 0]])  # 90 deg rotation
B = np.array([[1, 1], [0, 1]])   # Shear
C = np.array([[1, -1], [1, 0]])  # Custom

# 2. Calculate Intermediate "Mega-Moves"
AB = A @ B
BC = B @ C

# 3. Calculate Final Destinations
Path1_Final = A @ BC   # A * (BC)
Path2_Final = AB @ C   # (AB) * C

# --- PRINT THE MATH TO TERMINAL ---
print("--- INTERMEDIATE MATRICES ---")
print("Matrix (AB):\n", AB)
print("\nMatrix (BC):\n", BC)

print("\n--- FINAL DESTINATIONS ---")
print("Path 1 Matrix A(BC):\n", Path1_Final)
print("Path 2 Matrix (AB)C:\n", Path2_Final)

# --- VISUALIZE THE JOURNEYS ---
square = np.array([[0, 1, 1, 0, 0], 
                   [0, 0, 1, 1, 0]])

# Path 1 Steps
sq_after_BC = BC @ square
sq_final_path1 = A @ sq_after_BC

# Path 2 Steps
sq_after_C = C @ square
sq_final_path2 = AB @ sq_after_C

fig, axes = plt.subplots(2, 3, figsize=(15, 8))
plt.subplots_adjust(hspace=0.4)

# ROW 1: PATH 1 [ A(BC) ]
axes[0, 0].plot(square[0], square[1], 'k-o')
axes[0, 0].set_title("Start: Original Square")

axes[0, 1].plot(sq_after_BC[0], sq_after_BC[1], 'r-o')
axes[0, 1].set_title("Step 1: Apply (BC) Mega-move")

axes[0, 2].plot(sq_final_path1[0], sq_final_path1[1], 'g-o', lw=3)
axes[0, 2].set_title("Step 2: Apply A -> Final Path 1")

# ROW 2: PATH 2 [ (AB)C ]
axes[1, 0].plot(square[0], square[1], 'k-o')
axes[1, 0].set_title("Start: Original Square")

axes[1, 1].plot(sq_after_C[0], sq_after_C[1], 'b-o')
axes[1, 1].set_title("Step 1: Apply C")

axes[1, 2].plot(sq_final_path2[0], sq_final_path2[1], 'g-o', lw=3)
axes[1, 2].set_title("Step 2: Apply (AB) Mega-move -> Final Path 2")

# Formatting for all subplots
for ax in axes.flat:
    ax.grid(True); ax.axhline(0, color='black', lw=0.5); ax.axvline(0, color='black', lw=0.5)
    ax.set_xlim(-3, 3); ax.set_ylim(-3, 3)

plt.show()