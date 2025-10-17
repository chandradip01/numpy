import numpy as np
import matplotlib.pyplot as plt

# Generate x values from -10 to 10
x = np.linspace(-10, 10, 200)

# Define the parabola equation y = ax² + bx + c
a, b, c = 1, 0, 0   # You can change these values
y = a * x**2 + b * x + c

# Plot the parabola
plt.plot(x, y, color='blue', label='y = x²')

# Add labels and title
plt.title("Parabola: y = ax² + bx + c")
plt.xlabel("x-axis")
plt.ylabel("y-axis")

# Add grid and legend
plt.grid(True)
plt.legend()

# Show the graph
plt.show()