# import numpy as np

# # 1. Create a NumPy array (a vector of 5 integers)
# a = np.array([1, 2, 3, 4, 5])

# # 2. Print the array and its type
# print("Original Array 'a':", a)
# print("Type of 'a':", type(a))
# print("Shape of 'a':", a.shape)

# # 3. Perform a simple element-wise operation (squaring each element)
# b = a ** 2

# # 4. Print the result
# print("New Array 'b' (a squared):", b)
# import numpy as np

# # 1. Create a NumPy array (a vector of 5 integers)
# a = np.array([1, 2, 3, 4, 5])

# # 2. Print the array and its type
# print("Original Array 'a':", a)
# print("Type of 'a':", type(a))
# print("Shape of 'a':", a.shape)

# # 3. Perform a simple element-wise operation (squaring each element)
# b = a ** 2

# # 4. Print the result
# print("New Array 'b' (a squared):", b)
# Import libraries
import numpy as np
import matplotlib.pyplot as plt

# ---------- 2D Plot: y = sin(x) ----------
# Create array of x values
x = np.linspace(0, 2 * np.pi, 100)   # 100 points between 0 and 2π
y = np.sin(x)                        # y = sin(x)

# Plot the sine wave
plt.figure(figsize=(6,4))
plt.plot(x, y, 'b', linewidth=2)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of y = sin(x)')
plt.grid(True)
plt.show()


# ---------- 3D Surface Plot: z = x² + y² ----------
from mpl_toolkits.mplot3d import Axes3D  # for 3D plotting

# Create meshgrid for x and y
x = np.arange(-2, 2.1, 0.1)
y = np.arange(-2, 2.1, 0.1)
X, Y = np.meshgrid(x, y)

# Define z = x² + y²
Z = X**2 + Y**2

# Create 3D figure
fig = plt.figure(figsize=(6,5))
ax = fig.add_subplot(111, projection='3d')

# Plot surface
ax.plot_surface(X, Y, Z, cmap='viridis')

# Labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Surface: z = x² + y²')

plt.show()