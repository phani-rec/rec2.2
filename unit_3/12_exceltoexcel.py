from openpyxl import load_workbook

# Load an Excel workbook
wb = load_workbook('00_data.xlsx')

# Select the active sheet
sheet = wb.active

# Read a specific cell value (e.g., A2)
value = sheet['A2'].value
print(value)

# Write a value to a cell (e.g., A2)
sheet['A2'] = 'abc'

# Save the workbook after editing
wb.save('00_output2.xlsx')