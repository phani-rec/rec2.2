from openpyxl import load_workbook

# Load the existing workbook
wb = load_workbook('00_output.xlsx')

# Get the sheet you want to write to
sheet = wb['Sheet1']

# Add a new row of data
sheet.append(['David', 40, 'Houston'])

# Save the changes
wb.save('00_output.xlsx')
