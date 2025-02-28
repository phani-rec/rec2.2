import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'A': [10, 20, 30],
    'B': [100, 200, 300]
}, index=['a', 'b', 'c'])

# Reindex the DataFrame with a new index
new_index = ['c', 'b', 'a', 'd']  # Adding a new index 'd'
df_reindexed = df.reindex(new_index)

print(df_reindexed)

print('....Reindexing Columns....')

new_columns = ['B', 'A']
df_reindexed_columns = df.reindex(columns=new_columns)

print(df_reindexed_columns)

# Reindexing with missing data
print('Reindexing with missing data.....')
df_reindexed = df.reindex(['a', 'd', 'e', 'b', 'c'])
print(df_reindexed)

print('Reindexing and Filling Missing Values.....')
df_reindexed_filled = df.reindex(['a', 'd', 'e', 'b', 'c'], fill_value=0)

print(df_reindexed_filled)
