import polars as pl

# Some DataFrame named df

# [-------- FILTERING BY VALUE --------]

# Filter the data to include only rows where column 'value_col' is greater than 100
filtered_data = df.filter(pl.col('value_col') > 100)


# [-------- FILTERING USING CONDITIONS --------]
# Filtering is not null, Filtering numberic conditions, filtering nulls 
df = pl.DataFrame({
    'A': [1, 2, 4, None, 8],
    'B': ['clap', 'snare_drum', 'bass_drum', None, 'crash']
})

# Filter for rows where 'A' is greater than 2 and 'B' is not null
filtered = df.filter((pl.col('A') > 2) & pl.is_not_null(pl.col('B')))
print(filtered)

# Filter for rows where 'A' is null or 'B' is 'bass_drum'
filtered = df.filter((pl.col('A').is_null()) | (pl.col('B') == 'bass_drum'))
print(filtered)

# Filter for rows where 'A' is not null and 'B' is null
filtered = df.filter(pl.is_not_null(pl.col('A')) & pl.col('B').is_null())
print(filtered)



# [-------FILTERING TEST|TRAIN FROM COLUMN 'DATA' --------]
# CREATING 2 NEW COLUMNS(TRAIN & TEST) FOR ROWS WITH RESPECTIVE VALUES

# Create sample data
df = pl.DataFrame({
    'data': ['train', 'train', 'test', 'train', 'test', 'train','test','train'],
    'sample_name': ['j','u','p','i','t','e','r','s'],
    'sampe_numeric': [8,88,888,8888,88888,888888,8888888,88888888]
})

# Filter for rows where 'data' column contains 'train'
train_df = df.filter(pl.col('data').str.contains('train'))
print(train_df)

# Filter for rows where 'data' column contains 'test'
test_df = df.filter(pl.col('data').str.contains('test'))
print(test_df)

# Create new 'train' and 'test' columns based on filtered data
df = df.with_column(
    'train',
    pl.when(pl.col('data').str.contains('train'), True).otherwise(False)
).with_column(
    'test',
    pl.when(pl.col('data').str.contains('test'), True).otherwise(False)
)

# Delete original 'data' column
df = df.drop('data')

# Print the new df
print(df)
