import pandas as data
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = data.read_csv('F:\DEVL PROJECT\Spotify_Most_Streamed_Songs.csv')

# Inspect the first few rows of the DataFrame
print("First 5 rows:")
print(data.head())

# Inspect the last few rows of the DataFrame
print("\nLast 5 rows:")
print(data.tail())

# Get a concise summary of the DataFrame
print("\nDataFrame Info:")
data.info()

# Generate descriptive statistics
print("\nDescriptive Statistics:")
print(data.describe())

# Check for missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Fill missing values in 'in_spotify_playlists' with 0
data['in_spotify_playlists'].fillna(0, inplace=True)

# Drop unnecessary columns (for demonstration)
data_cleaned = data.drop(columns=['cover_url', 'in_apple_playlists', 'in_deezer_playlists'])

# Rename columns for easier access
data_cleaned.rename(columns={'released_year': 'Year', 'streams': 'Streams'}, inplace=True)

# Group by year and calculate total streams per year
streams_per_year = data_cleaned.groupby('Year')['Streams'].sum().reset_index()

# Plotting with Matplotlib
plt.figure(figsize=(30, 15))
plt.plot(streams_per_year['Year'], streams_per_year['Streams'], marker='o')
plt.title('Total Streams per Year')
plt.xlabel('Year')
plt.ylabel('Total Streams')
plt.grid()
plt.show()

# Plotting with Seaborn: Boxplot of streams by year
plt.figure(figsize=(30, 15))
sns.boxplot(data=data_cleaned, x='Year', y='Streams')
plt.title('Boxplot of Streams by Year')
plt.xlabel('Year')
plt.ylabel('Streams')
sns.set_style('whitegrid')
plt.show()

# Scatter plot to visualize relationship between danceability and streams
plt.figure(figsize=(30, 15))
sns.scatterplot(data=data_cleaned, x='danceability_%', y='Streams', palette='viridis', alpha=0.7)
plt.title('Danceability vs Streams')
plt.xlabel('Danceability (%)')
plt.ylabel('Streams')
plt.legend(title='Year', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()

# Univariate Analysis

# Histogram of Streams
plt.figure(figsize=(12, 6))
sns.histplot(data_cleaned['Streams'], bins=30, kde=True)
plt.title('Distribution of Streams')
plt.xlabel('Streams')
plt.ylabel('Frequency')
plt.grid()
plt.show()

data['in_spotify_playlists'] = data['in_spotify_playlists'].fillna(0)

# Group by artist and sum the streams
artist_streams = data.groupby('artist(s)_name')['streams'].sum().nlargest(5)

# Create a pie chart for the top 5 artists by total streams
plt.figure(figsize=(8, 8))
plt.pie(artist_streams, labels=artist_streams.index, autopct='%1.1f%%', startangle=140)
plt.title('Top 5 Artists by Total Streams')
plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular.
plt.show()

