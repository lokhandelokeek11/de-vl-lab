import matplotlib.pyplot as plt
import numpy as np

# Sample Data
x = np.linspace(0, 10, 100)  
y = np.sin(x)              

# Create a figure with specific size
plt.figure(figsize=(12, 10))

# 1. Line Plot
plt.subplot(3, 2, 1)  # 3 rows, 2 columns, first subplot
plt.plot(x, y, color='blue', linestyle='-', linewidth=2)
plt.title('Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.show()
