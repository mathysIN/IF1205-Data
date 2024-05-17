import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('abalone_data.csv')

# Check for missing values
missing_values = df.isnull().sum()
print('Missing values in each column:')
print(missing_values)

# Drop observations with missing values
df_cleaned = df.dropna()

# Verify that there are no missing values left
missing_values_after_cleanup = df_cleaned.isnull().sum()
print('Missing values in each column after cleanup:')
print(missing_values_after_cleanup)

# Optional: Display the cleaned DataFrame's shape to see the number of observations remaining
print(f'Number of observations after removing missing values: {df_cleaned.shape[0]}')
