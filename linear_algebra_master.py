# %% 1. Simple Vector
import numpy as np
import matplotlib.pyplot as plt

# The operation: Defining a single vector
v = np.array([3, 4])

print(f"Vector v: {v}")

# The visualization (Single = Arrow)
plt.figure(figsize=(5, 5))
plt.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='blue')

plt.xlim(-1, 5)
plt.ylim(-1, 5)
plt.grid(True, linestyle='--')
plt.axhline(0, color='black', lw=1)
plt.axvline(0, color='black', lw=1)
plt.title("1. Simple Vector")
plt.show()




# %%
# %% 2. Vector Addition
import numpy as np
import matplotlib.pyplot as plt

# The operation
v1 = np.array([2, 1])
v2 = np.array([1, 3])
v3 = v1 + v2  # Vector Addition

print(f"v1: {v1}")
print(f"v2: {v2}")
print(f"v1 + v2 = {v3}")

# The visualization
plt.figure(figsize=(5, 5))
# Plot v1
plt.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='blue', label='v1')
# Plot v2 starting from the tip of v1 (head-to-tail addition)
plt.quiver(v1[0], v1[1], v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='red', label='v2')
# Plot the result from origin to the final tip
plt.quiver(0, 0, v3[0], v3[1], angles='xy', scale_units='xy', scale=1, color='green', label='v1+v2')

plt.xlim(0, 4)
plt.ylim(0, 5)
plt.grid(True, linestyle='--')
plt.legend()
plt.title("2. Vector Addition")
plt.show()





# %%
# %% 3. Scaling
import numpy as np
import matplotlib.pyplot as plt

# The operation
v = np.array([2, 1.5])
scalar = 2.5
v_scaled = v * scalar

print(f"Original v: {v}")
print(f"Scaled by {scalar}: {v_scaled}")

# The visualization
plt.figure(figsize=(6, 6))
# Plot the scaled vector first (so it sits behind the original)
plt.quiver(0, 0, v_scaled[0], v_scaled[1], angles='xy', scale_units='xy', scale=1, color='red', label='Scaled Vector')
# Plot original vector
plt.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='blue', label='Original Vector')

plt.xlim(0, 6)
plt.ylim(0, 5)
plt.grid(True, linestyle='--')
plt.legend()
plt.title(f"4. Vector Scaled by {scalar}")
plt.show()



# %%
# %% 4. Span
import numpy as np
import matplotlib.pyplot as plt

# The operations
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



# %%
# %% 5. Linear Dependent vs Independent
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



# %%
# %% 6. Single = Arrow, Multiple = Points
import numpy as np
import matplotlib.pyplot as plt

# Data
single_vector = np.array([3, 4])
multiple_vectors = np.random.randn(100, 2) * 2 # 100 vectors (Dataset)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# Plot 1: Single Vector -> Arrow
ax1.quiver(0, 0, single_vector[0], single_vector[1], angles='xy', scale_units='xy', scale=1, color='blue')
ax1.set_title("Single Vector (Arrow)")
ax1.set_xlim(-1, 5); ax1.set_ylim(-1, 5); ax1.grid(True)

# Plot 2: Multiple Vectors -> Points
ax2.scatter(multiple_vectors[:, 0], multiple_vectors[:, 1], c='purple', alpha=0.6)
ax2.set_title("Multiple Vectors (Points / Scatter)")
ax2.set_xlim(-5, 5); ax2.set_ylim(-5, 5); ax2.grid(True)

plt.show()



# %%
# %% 7. Pythagorean Theorem (Vector Length)
import numpy as np
import matplotlib.pyplot as plt

# The operation
v = np.array([5, 3]) # x=5, y=3

# The Math: Length = sqrt(x^2 + y^2)
x_squared = v[0]**2
y_squared = v[1]**2
length_manual = np.sqrt(x_squared + y_squared)

# The built-in NumPy way
length_numpy = np.linalg.norm(v)

print(f"Vector Coordinates: x={v[0]}, y={v[1]}")
print(f"Manual Pythagoras: sqrt({x_squared} + {y_squared}) = {length_manual}")
print(f"NumPy norm result: {length_numpy}")

# The visualization (Forming the right triangle)
plt.figure(figsize=(6, 6))

# Main vector
plt.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='blue', label=f'Vector (Len={length_manual})')

# X component (Base)
plt.plot([0, v[0]], [0, 0], 'r--', lw=3, label=f'Base (x={v[0]})')
# Y component (Height)
plt.plot([v[0], v[0]], [0, v[1]], 'g--', lw=3, label=f'Height (y={v[1]})')

plt.xlim(-1, 5)
plt.ylim(-1, 4)
plt.grid(True, linestyle='--')
plt.legend()
plt.title("8. Calculating Vector Length via Pythagoras")
plt.show()



# %%
# %% 8. Linear Transformation Rules (Grid)
import numpy as np
import matplotlib.pyplot as plt

# Generate a grid of points
x, y = np.meshgrid(np.arange(-3, 4, 1), np.arange(-3, 4, 1))
grid_points = np.vstack([x.flatten(), y.flatten()])

# Define a transformation matrix (a slight stretch and tilt)
M = np.array([[1.5, 0.5], 
              [0.2, 1.2]])

# Apply transformation
transformed_grid = np.dot(M, grid_points)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# Original Grid
ax1.scatter(grid_points[0], grid_points[1], color='blue', s=10)
ax1.plot(0, 0, 'ro', markersize=8) # Mark the Origin
ax1.set_title("Original Grid (Origin is Red)")
ax1.grid(True); ax1.set_xlim(-6, 6); ax1.set_ylim(-6, 6)
ax1.axhline(0, color='black'); ax1.axvline(0, color='black')

# Transformed Grid
ax2.scatter(transformed_grid[0], transformed_grid[1], color='purple', s=10)
ax2.plot(0, 0, 'ro', markersize=8) # Origin stays in place!
ax2.set_title("Transformed (Lines Parallel, Origin Fixed)")
ax2.grid(True); ax2.set_xlim(-6, 6); ax2.set_ylim(-6, 6)
ax2.axhline(0, color='black'); ax2.axvline(0, color='black')

plt.show()



# %%
# %% 9. Specific Matrix [1,2; 2,4] applied to v=(x,y)
import numpy as np
import matplotlib.pyplot as plt

# The Matrix
M = np.array([[1, 2], 
              [2, 4]])

# The Vector (Let's pick x=1, y=2)
v = np.array([1, 2])

# Multiply
v_transformed = np.dot(M, v)

print("Matrix M:")
print(M)
print(f"Original Vector v: {v}")
print(f"Transformed Vector: {v_transformed}")

plt.figure(figsize=(6, 6))
# Plot original
plt.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='blue', label='Original v [1,2]')
# Plot transformed
plt.quiver(0, 0, v_transformed[0], v_transformed[1], angles='xy', scale_units='xy', scale=1, color='red', label='Transformed v [5,10]')

plt.xlim(-1, 6)
plt.ylim(-1, 11)
plt.grid(True, linestyle='--')
plt.legend()
plt.title("10. Matrix [1 2; 2 4] applied to Vector")
plt.show()




# %%
# %% 10. Multiply Matrix and Vector (Formula)
import numpy as np
import matplotlib.pyplot as plt

M = np.array([[3,  2], 
              [-2, 1]])
v = np.array([5, 7])

# The Math breakdown
x_new = (M[0,0] * v[0]) + (M[0,1] * v[1])
y_new = (M[1,0] * v[0]) + (M[1,1] * v[1])
v_result = np.array([x_new, y_new])

print("--- The Formula ---")
print(f"X_new = ({M[0,0]} * {v[0]}) + ({M[0,1]} * {v[1]}) = {x_new}")
print(f"Y_new = ({M[1,0]} * {v[0]}) + ({M[1,1]} * {v[1]}) = {y_new}")
print(f"Final Vector: {v_result}")

plt.figure(figsize=(7, 7))
plt.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='blue', label='Original [5,7]')
plt.quiver(0, 0, v_result[0], v_result[1], angles='xy', scale_units='xy', scale=1, color='red', label='Result [29,-3]')

plt.xlim(-5, 30) # Extended X axis to see 29
plt.ylim(-5, 10)
plt.grid(True, linestyle='--')
plt.axhline(0, color='black'); plt.axvline(0, color='black')
plt.legend()
plt.title("11. Matrix Multiplication Result")
plt.show()


# %%
# %% 11. 90 Degree Rotation Matrix
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


# %%
# %% 12. Shear Matrix
import numpy as np
import matplotlib.pyplot as plt

# A Horizontal Shear Matrix
Shear = np.array([[1, 1.5], 
                  [0, 1]])

# Create a square (4 corners)
square = np.array([[0, 2, 2, 0, 0], 
                   [0, 0, 2, 2, 0]])

# Apply Shear
sheared_square = np.dot(Shear, square)

plt.figure(figsize=(7, 5))
plt.plot(square[0], square[1], 'b-o', label='Original Square')
plt.plot(sheared_square[0], sheared_square[1], 'r--o', label='Sheared Square')

plt.xlim(-1, 6)
plt.ylim(-1, 3)
plt.grid(True, linestyle='--')
plt.axhline(0, color='black'); plt.axvline(0, color='black')
plt.legend()
plt.title("13. Horizontal Shear Transformation")
plt.show()


# %%
# %% 13. Linearly Dependent Matrix (Space Collapse)
import numpy as np
import matplotlib.pyplot as plt

# Dependent matrix (Row 2 is just Row 1 multiplied by -1)
M_dep = np.array([[ 1,  2], 
                  [-1, -2]])

print(f"Determinant: {np.linalg.det(M_dep)}")

# Create a cloud of 100 random 2D points (A 2D plane of data)
points = np.random.uniform(-5, 5, (2, 100))

# Apply the dependent matrix
collapsed_points = np.dot(M_dep, points)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Original 2D Cloud
ax1.scatter(points[0], points[1], color='blue', s=10)
ax1.set_title("Original Data (2D Plane)")
ax1.set_xlim(-15, 15); ax1.set_ylim(-15, 15)
ax1.grid(True); ax1.axhline(0, color='black'); ax1.axvline(0, color='black')

# Transformed Cloud (Collapsed!)
ax2.scatter(collapsed_points[0], collapsed_points[1], color='red', s=10)
ax2.set_title("Transformed Data (Collapsed to 1D Line)")
ax2.set_xlim(-15, 15); ax2.set_ylim(-15, 15)
ax2.grid(True); ax2.axhline(0, color='black'); ax2.axvline(0, color='black')

plt.show()


# %%
# %% 14. Rotation + Shear (Order Matters)
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


# %%
# %% 15. Step-by-Step 2D Associativity
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
# %%
# %% 16. Step-by-Step 3D Associativity
%matplotlib widget
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






# %% 17. Determinant 2D (Area)
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



# %%
# %% 18. Determinant 3D (Volume)
%matplotlib widget #this line is use to make interactive 3d instead of png
import numpy as np
import matplotlib.pyplot as plt

M_3d = np.array([
    [2, 0, 0],
    [0, 2, 0],
    [0, 0, 2]
])
# A 2x2x2 scaling matrix. Volume should increase by 2*2*2 = 8.
det_3d = np.linalg.det(M_3d)

print("--- 3D Determinant ---")
print(M_3d)
print(f"Determinant (Volume multiplier): {det_3d:.1f}")
print("A 1x1x1 unit cube becomes a 2x2x2 cube (Volume = 8).")

# --- VISUALIZATION ADDED BELOW ---
# Create a 1x1x1 unit cube
r = [0, 1]
x, y, z = np.meshgrid(r, r, r)
cube = np.vstack([x.flatten(), y.flatten(), z.flatten()])

# Transform the cube
transformed_cube = np.dot(M_3d, cube)

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Plot Original Cube (Small, Blue)
ax.scatter(cube[0], cube[1], cube[2], color='blue', s=50, label='Original (Vol=1)')
# Plot Transformed Cube (Large, Red)
ax.scatter(transformed_cube[0], transformed_cube[1], transformed_cube[2], color='red', s=100, alpha=0.5, label=f'Transformed (Vol={det_3d:.0f})')

ax.set_title("3D Determinant: Volume Expansion")
ax.set_xlim(0, 3); ax.set_ylim(0, 3); ax.set_zlim(0, 3)
ax.legend()
plt.show()


# %%
# %% 19. Inverse Matrix 2D
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


# %%
# %% 20. Column Space 2D
import numpy as np
import matplotlib.pyplot as plt

# Linearly Dependent Matrix (Col 2 is Col 1 * -1)
M = np.array([[1, -1], [2, -2]])

c1, c2 = M[:, 0], M[:, 1]

plt.figure(figsize=(5,5))
plt.quiver(0, 0, c1[0], c1[1], angles='xy', scale_units='xy', scale=1, color='b', label='Col 1')
plt.quiver(0, 0, c2[0], c2[1], angles='xy', scale_units='xy', scale=1, color='r', label='Col 2')
# Plot the 1D span line
plt.plot([-3, 3], [-6, 6], 'k--', alpha=0.5, label='Column Space (1D Line)')

plt.xlim(-4, 4); plt.ylim(-7, 7); plt.grid(True); plt.legend()
plt.title("21. Column Space of a Dependent Matrix")
plt.show()


# %%# %% 21. Rank in 2D
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



# %%
# %% 22. Null Space 2D
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


# %%# %% 23. 3D Inverse
%matplotlib widget
import numpy as np
import matplotlib.pyplot as plt

M = np.array([[1, 0, 2], [0, 1, 0], [3, 0, 1]])
v = np.array([5, 5, 5])

M_inv = np.linalg.inv(M)
v_transformed = np.dot(M, v)
v_restored = np.dot(M_inv, v_transformed)

print("--- 3D Inverse ---")
print(f"Original v: {v}")
print(f"Transformed: {v_transformed}")
print(f"Restored via Inverse: {np.round(v_restored, 1)}")

# --- VISUALIZATION ADDED BELOW ---
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Draw arrows for the vectors
ax.quiver(0, 0, 0, v[0], v[1], v[2], color='blue', lw=3, label='1. Original Vector')
ax.quiver(0, 0, 0, v_transformed[0], v_transformed[1], v_transformed[2], color='red', lw=2, label='2. Transformed (M)')
ax.quiver(0, 0, 0, v_restored[0], v_restored[1], v_restored[2], color='green', lw=5, alpha=0.5, label='3. Restored (M_inv)')

ax.set_title("3D Inverse: Green perfectly overlays Blue")
ax.set_xlim(0, 16); ax.set_ylim(0, 16); ax.set_zlim(0, 20)
ax.legend()
plt.show()



# %% 24, 25, 26. Spaces and Rank in 3D
%matplotlib widget
import numpy as np
import matplotlib.pyplot as plt

# A matrix where the 3rd column is exactly the 1st column
M_3d = np.array([
    [1, 2, 1],
    [3, 4, 3],
    [5, 6, 5]
])

print("--- 3D Matrix Properties ---")
print(M_3d)
print(f"Rank (26): {np.linalg.matrix_rank(M_3d)} (Spans a 2D plane in 3D space)")

# Null Space (27): Vector [-1, 0, 1] cancels out Col 1 and Col 3
null_v = np.array([-1, 0, 1])
print(f"Null Vector check: M * [-1, 0, 1] = {np.dot(M_3d, null_v)} (Null space exists!)")

# --- VISUALIZATION ADDED BELOW ---
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# 1. Plot the Column Space (Spans a 2D Plane)
c1, c2 = M_3d[:, 0], M_3d[:, 1]
ax.quiver(0, 0, 0, c1[0], c1[1], c1[2], color='blue', label='Col 1 & 3')
ax.quiver(0, 0, 0, c2[0], c2[1], c2[2], color='cyan', label='Col 2')

# Create a visual plane using the two independent columns
grid = np.linspace(-2, 2, 5)
c1_grid, c2_grid = np.meshgrid(grid, grid)
plane_x = c1[0]*c1_grid + c2[0]*c2_grid
plane_y = c1[1]*c1_grid + c2[1]*c2_grid
plane_z = c1[2]*c1_grid + c2[2]*c2_grid
ax.plot_surface(plane_x, plane_y, plane_z, color='blue', alpha=0.2)

# 2. Plot the Null Vector
ax.quiver(0, 0, 0, null_v[0], null_v[1], null_v[2], color='red', label='Null Vector [-1,0,1]')
# Plot where the Null Vector goes (The Origin)
ax.scatter(0, 0, 0, color='black', s=100, label='Origin (Where Null Vec lands)')

ax.set_title("Rank 2 Matrix: Col Space is a Plane, Null Vec maps to Origin")
ax.set_xlim(-6, 6); ax.set_ylim(-6, 6); ax.set_zlim(-6, 6)
ax.legend()
plt.show()


# %% 27. Independent System (det != 0) -> Unique Solution
import numpy as np
import matplotlib.pyplot as plt

# Eq 1: 2x + y = 5  => y = 5 - 2x
# Eq 2: x - y = 1   => y = x - 1
x_vals = np.linspace(0, 4, 100)
y1 = 5 - 2*x_vals
y2 = x_vals - 1

A = np.array([[2, 1], [1, -1]])
b = np.array([5, 1])
det = np.linalg.det(A)

# Calculate exact intersection
solution = np.linalg.solve(A, b)

plt.figure(figsize=(5,5))
plt.plot(x_vals, y1, '-b', label='2x + y = 5')
plt.plot(x_vals, y2, '-r', label='x - y = 1')
plt.plot(solution[0], solution[1], 'go', markersize=8, label=f'Solution {solution}')

plt.grid(True); plt.legend()
plt.title(f"30. Independent Lines (Det = {det:.1f})")
plt.show()


# %%
# %% 28. Dependent System (det = 0) -> No Solution
import numpy as np
import matplotlib.pyplot as plt

# Eq 1: 2x + y = 5  => y = 5 - 2x
# Eq 2: 4x + 2y = 4 => 2y = 4 - 4x => y = 2 - 2x
x_vals = np.linspace(0, 4, 100)
y1 = 5 - 2*x_vals
y2 = 2 - 2*x_vals

A = np.array([[2, 1], [4, 2]])
det = np.linalg.det(A)

print(f"Determinant: {det:.1f}. Because it's 0, no unique solution exists.")

plt.figure(figsize=(5,5))
plt.plot(x_vals, y1, '-b', label='2x + y = 5')
plt.plot(x_vals, y2, '-r', label='4x + 2y = 4')

plt.grid(True); plt.legend(); plt.ylim(0, 6)
plt.title(f"29. Dependent Lines (Det = {det:.1f}) = Parallel")
plt.show()



# %%
# %% 29. Dependent System 3D (Det = 0, No Solution)
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'widget')


import numpy as np
import matplotlib.pyplot as plt

# Eq 1: x + y + z = 1  => z = 1 - x - y
# Eq 2: x + y + z = 5  => z = 5 - x - y (Parallel to Eq 1)
# Eq 3: x - y + z = 2  => z = 2 - x + y

A = np.array([
    [1,  1, 1],
    [1,  1, 1], # Row 2 is exactly Row 1 (causes Det = 0)
    [1, -1, 1]
])

print(f"Determinant of A: {np.linalg.det(A):.2f}")
print("Because Det = 0, there is no single point where all 3 planes intersect!")

x, y = np.meshgrid(np.linspace(-5, 5, 10), np.linspace(-5, 5, 10))

z1 = 1 - x - y
z2 = 5 - x - y
z3 = 2 - x + y

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the surfaces
ax.plot_surface(x, y, z1, alpha=0.5, color='blue', label='Eq 1')
ax.plot_surface(x, y, z2, alpha=0.5, color='red', label='Eq 2 (Parallel)')
ax.plot_surface(x, y, z3, alpha=0.3, color='green')

ax.set_title("31. Dependent System (Det = 0) \nNotice the Red and Blue planes never touch!")
plt.show()



# %%
# %% 30. Independent System 3D (Det != 0, Unique Solution)
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'widget')

import numpy as np
import matplotlib.pyplot as plt

# Eq 1: x + y + z = 3     => z = 3 - x - y
# Eq 2: x - y + 2z = 4    => z = (4 - x + y) / 2
# Eq 3: 2x + y - z = 1    => z = 2x + y - 1

A = np.array([
    [1,  1,  1],
    [1, -1,  2],
    [2,  1, -1]
])
b = np.array([3, 4, 1])

det = np.linalg.det(A)
print(f"Determinant of A: {det:.2f}")

# Calculate the exact intersection point!
solution = np.linalg.solve(A, b)
print(f"The Unique Solution Point is: x={solution[0]}, y={solution[1]}, z={solution[2]}")

x, y = np.meshgrid(np.linspace(-2, 4, 10), np.linspace(-2, 4, 10))

z1 = 3 - x - y
z2 = (4 - x + y) / 2
z3 = 2*x + y - 1

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(x, y, z1, alpha=0.4, color='blue')
ax.plot_surface(x, y, z2, alpha=0.4, color='green')
ax.plot_surface(x, y, z3, alpha=0.4, color='yellow')

# Plot the exact solution point where they all cross
ax.scatter(solution[0], solution[1], solution[2], color='red', s=200, label='Solution Point')

ax.set_title(f"32. Independent System (Det = {det:.1f}) \nPlanes intersect at exactly one point!")
ax.legend()
plt.show()


# %%
# %% 31. Non-Square Matrices (Changing Dimensions)
import numpy as np
import matplotlib.pyplot as plt

# A 3x2 "Tall" Matrix. 
# It takes a 2D input [x, y] and outputs a 3D vector [x, y, z]
# In this case, z will be a combination of x and y (x + y)
M_tall = np.array([
    [1, 0],  # X output
    [0, 1],  # Y output
    [1, 1]   # Z output
])

print(f"Matrix Shape: {M_tall.shape} (3 Rows = 3D Output, 2 Columns = 2D Input)")

# Create a 2D Grid (Input Space)
x, y = np.meshgrid(np.linspace(-2, 2, 5), np.linspace(-2, 2, 5))
grid_2d = np.vstack([x.flatten(), y.flatten()]) # Shape: (2, 25)

# Multiply! This maps the 2D points into 3D space.
# (3x2) dot (2x25) = (3x25)
grid_3d = np.dot(M_tall, grid_2d)

fig = plt.figure(figsize=(12, 5))

# Plot 1: The Original 2D Input Space
ax1 = fig.add_subplot(121)
ax1.scatter(grid_2d[0], grid_2d[1], color='blue', s=40)
ax1.set_title("Input: 2D Space")
ax1.set_xlim(-3, 3); ax1.set_ylim(-3, 3)
ax1.grid(True); ax1.axhline(0, color='black'); ax1.axvline(0, color='black')

# Plot 2: The Transformed 3D Output Space
ax2 = fig.add_subplot(122, projection='3d')
ax2.scatter(grid_3d[0], grid_3d[1], grid_3d[2], color='red', s=40)
ax2.set_title("Output: Embedded into 3D Space")

# Set 3D limits to see the tilt clearly
ax2.set_xlim(-3, 3); ax2.set_ylim(-3, 3); ax2.set_zlim(-5, 5)

plt.show()

print("Notice that the result is a flat 2D plane, but it now 'lives' inside a 3D world!")
print("Because it's flat, it has no 3D Volume. If we tried to take a 3D determinant, it wouldn't work.")



# %%
# %% 32. Dot Product and Duality
%matplotlib widget
import numpy as np
import matplotlib.pyplot as plt

# 1. Define the vectors
v = np.array([3, 1])  # The vector that will define our 1D line
w = np.array([1, 2])  # The vector we are going to transform/project

# 2. Method A: Standard Dot Product (The Physics way)
dot_product = np.dot(v, w)

# 3. Method B: Duality / Matrix Multiplication (The Math way)
# We treat 'v' as a 1x2 transformation matrix that crushes 2D space onto a 1D line
matrix_v = np.array([[3, 1]]) # Shape: (1 row, 2 columns)
vector_w = np.array([[1],     # Shape: (2 rows, 1 column)
                     [2]])
transformation_result = matrix_v @ vector_w

# 4. Geometrically: Projection (The Visual way)
# Formula to find exactly where the shadow lands: (v • w / ||v||^2) * v
v_mag_sq = np.dot(v, v)
proj_w_on_v = (dot_product / v_mag_sq) * v

print("--- Chapter 9: Duality ---")
print(f"Vector v: {v}")
print(f"Vector w: {w}\n")
print(f"Method A (Dot Product): v • w = {dot_product}")
print(f"Method B (1x2 Matrix): [3 1] @ [1; 2] = {transformation_result[0][0]}")
print("Notice they are exactly the same mathematical operation!")

# --- VISUALIZATION ---
fig, ax = plt.subplots(figsize=(8, 6))

# Draw the infinite line spanned by v (This is the 1D space everything collapses onto)
x_vals = np.linspace(-2, 4, 100)
y_vals = (v[1]/v[0]) * x_vals
ax.plot(x_vals, y_vals, 'k--', alpha=0.4, label='1D Number Line (Span of v)')

# Draw the original vectors
ax.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='blue', label='Vector v [3,1]')
ax.quiver(0, 0, w[0], w[1], angles='xy', scale_units='xy', scale=1, color='red', label='Vector w [1,2]')

# Draw the projection (The shadow of w landing on v)
ax.quiver(0, 0, proj_w_on_v[0], proj_w_on_v[1], angles='xy', scale_units='xy', scale=1, color='green', lw=4, alpha=0.7, label='Projection of w onto v')

# Draw the dashed line showing the 'shadow' dropping straight down at a perfect 90-degree angle
ax.plot([w[0], proj_w_on_v[0]], [w[1], proj_w_on_v[1]], 'k:', lw=2, label='Projection path (90° Angle)')

ax.set_xlim(-1, 4)
ax.set_ylim(-1, 3)
ax.axhline(0, color='black', lw=0.5)
ax.axvline(0, color='black', lw=0.5)
ax.grid(True)
ax.set_title(f"Duality: Dot Product (Projection) = Matrix Transformation = {dot_product}")
ax.legend()
plt.show()
f# %%
