import pandas as pd

df=pd.read_excel('C:\\Users\\REC\\Desktop\\trail.xlsx')
#print(df)
print(list(df.columns.values))
 
# Step 3: Display the values of column B
print(df)
data= df.sort_values(["Branch","Name"], ascending=False)

# Convert the data to a DataFrame
out = pd.DataFrame(data)


# Write the DataFrame to an Excel file
out.to_excel("out14.xlsx", index=False, sheet_name='Sheet1')  # index=False avoids writing the row numbers

