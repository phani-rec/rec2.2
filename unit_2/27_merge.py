import pandas as pd

# Creating the DataFrames
df1 = pd.DataFrame({
    'Fruit': ['Apple', 'Banana', 'Cherry'],
    'Color': ['Red', 'Yellow', 'Red'],
    'Origin': ['USA', 'Ecuador', 'Turkey']
})

df2 = pd.DataFrame({
    'Fruit': ['Apple', 'Banana', 'Mango'],
    'Price': [1.2, 0.5, 1.5],
    'Store': ['Walmart', 'Costco', 'Trader Joe\'s']
})
print('-----merge-----')
# Merge based on 'Fruit' column (inner join by default)
merged_df = pd.merge(df1, df2, on='Fruit', how='inner')
print(merged_df)
