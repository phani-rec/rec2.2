# Importing pandas and numpy
import pandas as pd
import numpy as np

# Sample DataFrame with missing values
data = {'First Score': [None, 90, np.nan, 95],
        'Second Score': [30, 45, 56, np.nan],
        'Third Score': [np.nan, 40, 80, 98]}

df = pd.DataFrame(data)

# Checking for missing values using isnull()
missing_values = df.isnull()

print(missing_values)
