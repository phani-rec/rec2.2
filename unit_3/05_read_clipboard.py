import pandas as pd

# Read the clipboard data into a pandas DataFrame
df = pd.read_clipboard()

# Display the content of the DataFrame
print(df)

'''
Name    Age    Country
Alice   30     USA
Bob     25     Canada
Charlie 35     UK
copy the table and execute the code
'''