from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt
# Load the Iris dataset
iris = load_iris()

# Create a DataFrame from the dataset
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

# Add the target variable (species)
iris_df['target'] = iris.target

# Display the first few rows of the DataFrame
print("Printing first 5 values: ")
print(iris_df.head())

print("Printing the info of the dataset: ")
print(iris_df.info())

print("Printing the description of the dataset: ")
print(iris_df.describe())


#Visualization with matplotlib and seaborn

#1. Scatter plot
# Using matplotlib

iris_df['species'] = iris.target

# Create a scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(iris_df['sepal length (cm)'], iris_df['sepal width (cm)'], c=iris_df['species'], cmap='viridis')
plt.title('Scatter Plot: Sepal Length vs Sepal Width (Matplotlib)')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.colorbar(label='Species')
plt.show()

#Using seaborn
import seaborn as sns

# Create a scatter plot using Seaborn
plt.figure(figsize=(8, 6))
sns.scatterplot(x='sepal length (cm)', y='sepal width (cm)', hue='species', data=iris_df, palette='viridis')
plt.title('Scatter Plot: Sepal Length vs Sepal Width (Seaborn)')
plt.show()