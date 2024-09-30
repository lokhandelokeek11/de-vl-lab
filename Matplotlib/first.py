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

# 2. Bar Plot
categories = ['A', 'B', 'C', 'D']
values = [10, 20, 15, 25]
plt.subplot(3, 2, 2)  # Second subplot
plt.bar(categories, values, color='orange')
plt.title('Bar Plot')
plt.xlabel('Categories')
plt.ylabel('Values')

# 3. Scatter Plot
x_scatter = np.random.rand(50) * 10
y_scatter = np.random.rand(50) * 10
plt.subplot(3, 2, 3)  # Third subplot
plt.scatter(x_scatter, y_scatter, color='green', s=100)
plt.title('Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# 4. Histogram
data = np.random.randn(1000)  # Generate random data
plt.subplot(3, 2, 4)  # Fourth subplot
plt.hist(data, bins=30, color='purple', alpha=0.7)
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')

# 5. Pie Chart
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
plt.subplot(3, 2, 5)  # Fifth subplot
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title('Pie Chart')

# 6. Box Plot
data_box = [np.random.normal(0, std, 100) for std in range(1, 4)] 
plt.subplot(3, 2, 6)  # Sixth subplot
plt.boxplot(data_box)
plt.title('Box Plot')
plt.xlabel('Distribution')
plt.ylabel('Value')

# Adjust layout to prevent overlap
plt.tight_layout()

# Show all plots
plt.show()