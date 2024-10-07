import pandas as pd

titanic = pd.read_csv(r'C:/Users/lokha/Downloads/Titanic.csv')


print("First 5 rows of the dataset:")
print(titanic.head())
print("\nLast 5 rows of the dataset:")
print(titanic.tail())
print(titanic)

print("\nShape of the dataset (rows, columns):", titanic.shape)

print("\nColumn names in the dataset:")
print(titanic.columns)


# Data Cleaning Steps
# 1. Handle Missing Values

titanic['age'].fillna(titanic['age'].median(), inplace=True)

# Drop 'cabin' column due to too many missing values
titanic.drop('cabin', axis=1, inplace=True)

# Drop rows with missing 'embarked' values
titanic.dropna(subset=['embarked'], inplace=True)

# 2. Remove Duplicates
titanic.drop_duplicates(inplace=True)

# 4. Remove Outliers Using IQR Method
Q1 = titanic['fare'].quantile(0.25)  # First quartile
Q3 = titanic['fare'].quantile(0.75)  # Third quartile
IQR = Q3 - Q1  # Interquartile range

# Define bounds for outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Filter out outliers from the dataset based on 'Fare'
titanic_no_outliers = titanic[(titanic['fare'] >= lower_bound) & (titanic['fare'] <= upper_bound)]

# Display the cleaned data without outliers
print("\nCleaned Data (Outliers Removed):")
print(titanic_no_outliers.head())
print("Cleaned Last 5 rows of dataset")
print(titanic.tail())

# Show the shape of the original and cleaned datasets
print("\nOriginal dataset shape:", titanic.shape)
print("Cleaned dataset shape:", titanic_no_outliers.shape)

