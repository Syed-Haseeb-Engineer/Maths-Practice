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