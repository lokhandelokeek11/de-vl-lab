import pandas as pd

pd = pd.read_csv('F:\datasets\olympics.zip')

 # Display first few rows     
print("Data of first few rows: ")
print(pd.head())

print()
# Display the first 10 rows
print("Data of first few rows: ")
print(pd.head(10))  

print()

# Display the last 5 rows
print("Data of last few rows: ")
print(pd.tail())  

print()

# Display the last 10 rows
print("Data of last 10 rows: ")
print(pd.tail(10))  

print()

# Display information about the DataFrame
print("Info: ")
print(pd.info()) 

# Get summary statistics for numeric columns
print("Summary for numeric coloumns: ")
print(pd.describe())
# Get summary statistics for all columns 
 
print("Summary for all : ")
print(pd.describe(include='all'))  

 # Count of missing values for each column
print(pd.isnull().sum()) 


  # Sort by 'column_name' in ascending order
print("Sorted data : ")
sorted_data = pd.sort_values('gender')
