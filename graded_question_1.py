import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('abalone_data.csv')

# Display the first few rows of the DataFrame to get familiar with the data
print(df.head())

# Get the number of observations and variables
num_observations = df.shape[0]
num_variables = df.shape[1]

print(f'Number of observations: {num_observations}')
print(f'Number of variables: {num_variables}')
