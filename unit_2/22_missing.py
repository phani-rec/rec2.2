# Creating a DataFrame with NaN values
import pandas as pd
df_missing = pd.DataFrame({
    'Name': ['Alice', 'Bob', None],
    'Age': [25, None, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
})

# Checking for missing values
print(df_missing.isnull())

# Filling missing values with a default value
df_missing['Age'] = df_missing['Age'].fillna(df_missing['Age'].mean())
print(df_missing)
