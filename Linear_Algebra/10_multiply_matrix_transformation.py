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