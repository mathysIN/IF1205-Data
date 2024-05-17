import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
df = pd.read_csv('abalone_data.csv')

# Display the first few rows of the DataFrame to get familiar with the data
print(df.head())

# Get the number of observations and variables
num_observations = df.shape[0]
num_variables = df.shape[1]

print(f'Number of observations: {num_observations}')
print(f'Number of variables: {num_variables}')

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

# Calculate descriptive statistics
descriptive_stats = df_cleaned.describe(include='all')
print('Descriptive statistics:')
print(descriptive_stats)

# Identify qualitative variables
qualitative_vars = df_cleaned.select_dtypes(include=['object']).columns
print(f'Qualitative variables: {qualitative_vars}')

# Get categories for each qualitative variable
for var in qualitative_vars:
    categories = df_cleaned[var].unique()
    print(f'Categories for {var}: {categories}')

# Visualize the distribution of numerical variables using histograms
df_cleaned.hist(figsize=(15, 10))
plt.suptitle('Histograms of Numerical Variables')
plt.show()

# Visualize relationships between numerical variables using scatter plots
sns.pairplot(df_cleaned)
plt.suptitle('Scatter Plots of Numerical Variables', y=1.02)
plt.show()

# Visualize the distribution of numerical variables using boxplots
plt.figure(figsize=(15, 10))
for i, column in enumerate(df_cleaned.select_dtypes(include=['number']).columns):
    plt.subplot(3, 3, i + 1)
    sns.boxplot(y=df_cleaned[column])
    plt.title(f'Boxplot of {column}')
plt.tight_layout()
plt.show()

# Visualize the distribution of qualitative variables
for var in qualitative_vars:
    sns.countplot(x=var, data=df_cleaned)
    plt.title(f'Distribution of {var}')
    plt.show()
