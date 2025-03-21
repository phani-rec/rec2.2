import pandas as pd

with pd.ExcelWriter('multiple_sheets.xlsx', engine='openpyxl') as writer:
    df1 = pd.DataFrame({'Name': ['Alice', 'Bob'], 'Age': [25, 30]})
    df2 = pd.DataFrame({'City': ['NY', 'LA'], 'Population': [8000000, 4000000]})

    # Write each DataFrame to a different sheet
    df1.to_excel(writer, sheet_name='Sheet1', index=False)
    df2.to_excel(writer, sheet_name='Sheet2', index=False)
