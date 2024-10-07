import matplotlib.pyplot as plt
import numpy as np

# Sample Data
x = np.linspace(0, 10, 100)  
y = np.sin(x)              

# Create a figure with specific size
plt.figure(figsize=(12, 10))

data_box = [np.random.normal(0, std, 100) for std in range(1, 4)] 
plt.subplot(3, 2, 6)  # Sixth subplot
plt.boxplot(data_box)
plt.title('Box Plot')
plt.xlabel('Distribution')
plt.ylabel('Value')
plt.show()