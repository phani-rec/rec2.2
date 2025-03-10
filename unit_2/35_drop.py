import pandas as pd
import numpy as np
# importing pandas as pd 
import pandas as pd
  
# Creating the dataframe  
df = pd.DataFrame({"A": [12, 4, 5, None, 1], 
                   "B": [None, 2, 54, 3, None], 
                   "C": [20, 16, None, 3, 8], 
                   "D": [14, 3, None, None, 6]}) 
  
# Print the dataframe 
print(df)

#Replace NULL values with the number 999:
print(df.fillna(999))

print(df.bfillna(88))

