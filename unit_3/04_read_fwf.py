import pandas as pd

# Read the fixed-width file
df = pd.read_fwf('00_data.fwf')

# Display the content
print(df)
