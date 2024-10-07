import matplotlib.pyplot as plt
import numpy as np

# Sample Data
x = np.linspace(0, 10, 100)  
y = np.sin(x)              

# Create a figure with specific size
plt.figure(figsize=(12, 10))

data = np.random.randn(1000)  # Generate random data
plt.subplot(3, 2, 4)  # Fourth subplot
plt.hist(data, bins=30, color='purple', alpha=0.7)
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()