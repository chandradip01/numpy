import numpy as np

# 1. Create a NumPy array (a vector of 5 integers)
a = np.array([1, 2, 3, 4, 5])

# 2. Print the array and its type
print("Original Array 'a':", a)
print("Type of 'a':", type(a))
print("Shape of 'a':", a.shape)

# 3. Perform a simple element-wise operation (squaring each element)
b = a ** 2

# 4. Print the result
print("New Array 'b' (a squared):", b)
import numpy as np
import matplotlib.pyplot as plt

# 1. Define the range for x
x = np.linspace(-5, 5, 100) # 100 points between -5 and 5

# 2. Define the equation for a parabola (y = x^2)
y = x**2

# 3. Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x, y, label=r'$y = x^2$', color='blue')

# 4. Add labels and title
plt.title('Plot of a Parabola ($y = x^2$)')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.grid(True)
plt.legend()

# 5. Save the figure (or use plt.show() if running locally)
plt.savefig('parabola_plot.png')