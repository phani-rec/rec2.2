import pandas as pd

# Sample data (as a Python dictionary or list of lists)
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

# Convert the data to a DataFrame
df = pd.DataFrame(data)

# Specify the output Excel file path
output_file = '00_output.xlsx'

# Write the DataFrame to an Excel file
df.to_excel(output_file, index=False, sheet_name='Sheet1')  # index=False avoids writing the row numbers
