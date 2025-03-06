import pandas as pd
import numpy as np

dict = {'First Score': [100, 90, np.nan, 95],
        'Second Score': [30, 40, 56, np.nan],
        'Third Score': [None, 40, 80, 98]}

df = pd.DataFrame(dict)

# Filling missing values with 0
df.fillna(0)
print(df)
print(df.fillna(9))
print(df.replace(np.nan, 100))
print(df.replace([100, 40,np.nan], [900, 80,'a']))
print(df.interpolate())

