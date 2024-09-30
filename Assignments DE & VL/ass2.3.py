import pandas as pd
import matplotlib as mtlb

# Define the file path
df = pd.read_csv(r"C:\Users\lokha\Desktop\sample.csv")


print(df)
print(df.head())
print(df.info())

#Data Cleaning 
# Drop Duplicates

df = df.drop_duplicates()

#Drop rows with missing values

df = df.dropna()

print(df.isnull().sum())


#Histogram
df['Age'].hist()
data_plot= df['Gender']
mtlb.hist(data_plot,bins = 10, color = 'blue',alpha = 0.8)
mtlb.show()