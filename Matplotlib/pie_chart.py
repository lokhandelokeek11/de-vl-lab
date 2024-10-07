import matplotlib.pyplot as plt
import numpy as np

# Sample Data
x = np.linspace(0, 10, 100)  
y = np.sin(x)              

# Create a figure with specific size
plt.figure(figsize=(12, 10))

sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
plt.subplot(3, 2, 5)  # Fifth subplot
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title('Pie Chart')
plt.show()