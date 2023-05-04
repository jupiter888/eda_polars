import polars as pl

# Extract: Read Excel file into a Polars DataFrame
df = pl.read_excel('input_file.xlsx')

# Transform: Perform data cleaning and transformation
df = df.select(['column1', 'column2', 'column3']) # Select only certain columns
df = df.filter(pl.col('column1') > 0) # Filter rows based on a condition
df = df.fill_nulls(0) # Fill missing values with zeros
df = df.cast({'column2': pl.Int64}) # Convert column2 to integer data type
df['column4'] = df['column1'] + df['column3'] # Add a new column based on the existing columns

# Load: Write transformed data to a new Excel file
pl.write_excel(df, 'output_file.xlsx')
