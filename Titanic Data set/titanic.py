import pandas as pd

titanic = pd.read_csv('C:/Users/lokha/Downloads/Titanic.csv')

print(titanic.head())
print(titanic.tail())

# Get the number of rows and columns
print(titanic.shape)

# List all column names
print(titanic.columns)

