import polars as pl

# Some DataFrame named df

# Fill missing values with mean of column
df_mean = df.fill_nulls(df.mean())

# Fill missing values with median of column
df_median = df.fill_nulls(df.median())
