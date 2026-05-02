import numpy as np
import matplotlib.pyplot as plt

# 1. Define Base Matrices (Kept simple so visuals stay clean)
A = np.array([[1, 0, 0], [0, 0, -1], [0, 1, 0]]) # Rotate around X
B = np.array([[1, 1, 0], [0, 1, 0], [0, 0, 1]])  # Shear XY
C = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]])  # Swap X and Y

# 2. Calculate Intermediates
AB = A @ B
BC = B @ C

Path1_Final = A @ BC
Path2_Final = AB @ C

print("--- 3D INTERMEDIATE MATRICES ---")
print("Matrix (AB):\n", AB)
print("\nMatrix (BC):\n", BC)

# --- VISUALIZE THE JOURNEYS ---
r = [0, 1]
x, y, z = np.meshgrid(r, r, r)
cube = np.vstack([x.flatten(), y.flatten(), z.flatten()])

# Path 1 Steps
cube_after_BC = BC @ cube
cube_final_path1 = A @ cube_after_BC

# Path 2 Steps
cube_after_C = C @ cube
cube_final_path2 = AB @ cube_after_C

fig = plt.figure(figsize=(15, 8))

def plot_cube(ax_num, data, title, color):
    ax = fig.add_subplot(2, 3, ax_num, projection='3d')
    ax.scatter(data[0], data[1], data[2], color=color, s=40)
    ax.set_title(title)
    ax.set_xlim([-2, 2]); ax.set_ylim([-2, 2]); ax.set_zlim([-2, 2])

# ROW 1: PATH 1
plot_cube(1, cube, "Start: Original Cube", "black")
plot_cube(2, cube_after_BC, "Step 1: Apply (BC)", "red")
plot_cube(3, cube_final_path1, "Final Path 1: A(BC)", "green")

# ROW 2: PATH 2
plot_cube(4, cube, "Start: Original Cube", "black")
plot_cube(5, cube_after_C, "Step 1: Apply C", "blue")
plot_cube(6, cube_final_path2, "Final Path 2: (AB)C", "green")

plt.tight_layout()
plt.show()
