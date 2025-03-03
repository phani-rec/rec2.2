import pandas as pd 
df = pd.DataFrame({ 
'A': [1, 2, 2, 3, 4], 
'B': [5, 6, 7, 8, 9], 
'C': [1, 1, 1, 1, 1] 
}) 
df['A_rank'] = df['A'].rank() 
print(df)
