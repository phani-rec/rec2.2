import pandas as pd
import numpy as np

dict = {'First Score': [None, np.nan, np.nan, 95],
        'Second Score': [30, np.nan, 45, 56],
        'Third Score': [52, np.nan, 80, 98],
        'Fourth Score': [np.nan, np.nan, np.nan, 65]}

df = pd.DataFrame(dict)

print(df)

# Drop rows with at least one missing value
print(df.dropna(), end='....\n')
# Drop columns with at least one missing value
print(df.dropna(axis=1), end='---\n')
# Drop rows where all values are missing
df.dropna(how='all')
print(df.dropna(how='all'), end='****\n')