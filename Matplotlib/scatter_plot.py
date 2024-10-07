import matplotlib.pyplot as plt
import numpy as np

# Sample Data
x = np.linspace(0, 10, 100)  
y = np.sin(x)              

# Create a figure with specific size
plt.figure(figsize=(12, 10))

x_scatter = np.random.rand(50) * 10
y_scatter = np.random.rand(50) * 10
plt.subplot(3, 2, 3)  # Third subplot
plt.scatter(x_scatter, y_scatter, color='green', s=100)
plt.title('Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()