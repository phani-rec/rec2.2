import pandas as pd

# Creating an Index with a list
index1 = pd.Index([1, 2, 3, 4, 5])
print(index1)


# Setting a column as the index
df = pd.DataFrame({
    'City': ['New York', 'Los Angeles', 'Chicago'],
    'Population': [8000000, 4000000, 2700000]
})

df = df.set_index('City')
print(df)


# Creating a MultiIndex
arrays = [
    ['A', 'A', 'B', 'B'],
    ['one', 'two', 'one', 'two']
]

multi_index = pd.MultiIndex.from_arrays(arrays, names=('letter', 'number'))

df2 = pd.DataFrame({
    'value': [10, 20, 30, 40]
}, index=multi_index)

print(df2)

# Check type of the index
print('type of the index ',type(df2.index))

# Check the length of the index
print('the length of the index ',len(df2.index))

# Check the values in the index
print('the values in the index',df2.index.values)
