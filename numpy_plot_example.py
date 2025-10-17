# Import libraries
import sys, os
# Prevent local files named 'numpy.py' or 'matplotlib.py' in the same folder from shadowing the real installed packages.
_script_dir = os.path.dirname(os.path.abspath(__file__))
_removed_from_path = False
if _script_dir in sys.path:
    try:
        sys.path.remove(_script_dir)
        _removed_from_path = True
    except ValueError:
        _removed_from_path = False

import numpy as np
import matplotlib.pyplot as plt

# Restore sys.path so other imports (or relative imports) still work
if _removed_from_path:
    sys.path.insert(0, _script_dir)

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