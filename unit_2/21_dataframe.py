# Merging two DataFrames based on a common column
import pandas as pd
df1 = pd.DataFrame({
    'Name': ['Alice', 'Bob'],
    'Age': [25, 30]
})

df2 = pd.DataFrame({
    'Name': ['Alice', 'Bob'],
    'City': ['New York', 'Los Angeles']
})

merged_df = pd.merge(df1, df2, on='Name')
print(merged_df)
