#Create a DataFrame
import pandas as pd
df1 = pd.read_csv(r"")


print(df1)
print()

print("Head:\n",df1.head())
print()

print("Tail:\n",df1.tail())
print()

print("Describe:\n",df1.describe())
print()

print("Min:\n", df1.min())
print()

print("Max:\n",df1.max())
print()

print("Info:\n",df1.info())
print()

# Selecting a column
print(pd['Name'])
print()

# Selecting Multiple Columns
print(pd[['Name', 'Age']]) #double square brackets are needed 
print()

# Selecting rows by index
print(pd.loc[0]) #selecting row with index 0
print()

# Selecting with condition
print(pd[pd['Age'] > 30])
print()

# Selecing rows by index position
print(pd.iloc[0]) #first row
print(pd.iloc[0]) # second to third rows
