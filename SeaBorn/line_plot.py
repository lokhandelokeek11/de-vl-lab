import seaborn as sns
import matplotlib.pyplot as plt

# Load the built-in 'tips' dataset
tips = sns.load_dataset("tips")

print(tips.head())

# Set the theme for the plots
sns.set_theme(style="whitegrid")

# 1. Line Plot
plt.figure(figsize=(10, 6))
sns.lineplot(x="total_bill", y="tip", data=tips)
plt.title("Line Plot: Total Bill vs Tip")
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.show()

# 2. Scatter Plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x="total_bill", y="tip", hue="day", data=tips)
plt.title("Scatter Plot: Total Bill vs Tip by Day")
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.show()

# 3. Bar Plot
plt.figure(figsize=(10, 6))
sns.barplot(x="day", y="total_bill", data=tips)
plt.title("Bar Plot: Average Total Bill by Day")
plt.xlabel("Day")
plt.ylabel("Average Total Bill")
plt.show()

# 4. Histogram and KDE Plot
plt.figure(figsize=(10, 6))
sns.histplot(tips['total_bill'], bins=30, kde=True)
plt.title("Histogram and KDE: Total Bill Distribution")
plt.xlabel("Total Bill")
plt.ylabel("Frequency")
plt.show()

# 5. Box Plot
plt.figure(figsize=(10, 6))
sns.boxplot(x="day", y="total_bill", data=tips)
plt.title("Box Plot: Total Bill by Day")
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.show()

# 6. Violin Plot
plt.figure(figsize=(10, 6))
sns.violinplot(x="day", y="total_bill", data=tips)
plt.title("Violin Plot: Total Bill by Day")
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.show()

# 7. Pair Plot
sns.pairplot(tips)
plt.suptitle("Pair Plot: Relationships Between Variables", y=1.02)
plt.show()

# 8. Heatmap (for visualizing correlation matrix)
correlation = tips.corr()
plt.figure(figsize=(10, 6))
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Heatmap: Correlation Matrix of Tips Dataset")
plt.show()