import numpy as np
import matplotlib.pyplot as plt

# Generate x values from -10 to 10
x = np.linspace(-10, 10, 200)

# Define the parabola equation: y = ax^2 + bx + c
a, b, c = 1, 0, 0
y = a * x**2 + b * x + c

# Plot the parabola
plt.plot(x, y, label="y = x²", color='blue')

# Add labels and title
plt.title("Parabola using NumPy and Matplotlib")
plt.xlabel("x-axis")
plt.ylabel("y-axis")

# Add grid and legend
plt.grid(True)
plt.legend()

# Show the plot
plt.show()