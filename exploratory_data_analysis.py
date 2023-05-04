import polars as pl

# Create a DataFrame from an existing excel file 
df = pl.read_excel('input_file.xlsx')

# Get column names
col_names = df.columns

# Get row count
row_count = len(df)

# Get the sum of missing values
missing_values_sum = df.is_null().sum().sum()

# Print the results
print("Column names:", col_names)
print("Row count:", row_count)
print("Sum of missing values:", missing_values_sum)

