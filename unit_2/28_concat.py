import pandas as pd

df1 = pd.DataFrame({'Roll Number': [101, 102, 103],'Name': ['Alice', 'Bob', 'Charlie'],'Marks': [85, 92, 78]})
df2 = pd.DataFrame({'Roll Number': [104, 105, 106],'Name': ['David', 'Eve', 'Frank'],'Marks': [88, 95, 82]})

# Concatenating the two DataFrames
concatenated_df = pd.concat([df1, df2], ignore_index=True)
print(concatenated_df)
