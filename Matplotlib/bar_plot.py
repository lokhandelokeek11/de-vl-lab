import matplotlib.pyplot as plt
import numpy as np

# Sample Data
x = np.linspace(0, 10, 100)  
y = np.sin(x)              

# Create a figure with specific size
plt.figure(figsize=(12, 10))

#  Bar Plot
categories = ['A', 'B', 'C', 'D']
values = [10, 20, 15, 25]
plt.subplot(3, 2, 2)  
plt.bar(categories, values, color='orange')
plt.title('Bar Plot')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()