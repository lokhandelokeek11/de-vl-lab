import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#Load dataset 

df = sns.load_dataset('titanic')

df.head()
print(df.head())

print(f"No of record present in given dataset is: {df.shape[0]}")
print(f"No of attributes present in given dataset is: {df.shape[1]}")

df.sample(5)
print(df.sample())

print("Printing the info of dataset: ")
print(df.info())

print("Printing the description of dataset: ")
print(df.describe())

print("Printing description with objects")
print(df.describe(include = 'object'))


# Check for missing values
missing_values = df.isnull().sum()
print("Missing Values:\n", missing_values[missing_values > 0])

# Visualize missing values using a heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title('Missing Values Heatmap')
plt.show()

#Duplicate values

df.duplicated().sum()


df.dropna(inplace=True)


df.duplicated().sum()


#Univariate analysis
# Distribution of Age
plt.figure(figsize=(10, 6))
sns.histplot(df['age'].dropna(), bins=30, kde=True)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Distribution of Fare
plt.figure(figsize=(10, 6))
sns.histplot(df['fare'].dropna(), bins=30, kde=True)
plt.title('Fare Distribution')
plt.xlabel('Fare')
plt.ylabel('Frequency')
plt.show()


#Count plot for 'class'
plt.figure(figsize=(10,6))
sns.countplot(data = df , x='class', palette='Set2')
plt.title('Count by passengers by class: ')
plt.xlabel('class')
plt.ylabel('count')
plt.show()

#Count plot for 'age'
plt.figure(figsize=(20,15))
sns.countplot(data = df , x='age', palette='Set2')
plt.title('Count by passengers by age: ')
plt.xlabel('age')
plt.ylabel('count')
plt.show()

#pie chart 

# Create age bins
age_bins = pd.cut(df['age'], bins=[0, 12, 20, 30, 40, 50, 60, 70], right=False)
age_distribution = age_bins.value_counts()

plt.figure(figsize=(8, 8))
plt.pie(age_distribution, labels=age_distribution.index.astype(str), autopct='%1.1f%%', startangle=140)
plt.title('Age Distribution of Passengers')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()