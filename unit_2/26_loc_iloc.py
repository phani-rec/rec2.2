import pandas as pd
# From a dictionary
# importing the module 
import pandas as pd 

# creating a sample dataframe 
data = pd.DataFrame({'Brand': ['Maruti', 'Hyundai', 'Tata', 
							'Mahindra', 'Maruti', 'Hyundai', 
							'Renault', 'Tata', 'Maruti'], 
					'Year': [2012, 2014, 2011, 2015, 2012, 
							2016, 2014, 2018, 2019], 
					'Kms Driven': [50000, 30000, 60000, 
									25000, 10000, 46000, 
									31000, 15000, 12000], 
					'City': ['Gurgaon', 'Delhi', 'Mumbai', 
							'Delhi', 'Mumbai', 'Delhi', 
							'Mumbai', 'Chennai', 'Ghaziabad'], 
					'Mileage': [28, 27, 25, 26, 28, 
								29, 24, 21, 24]}) 


df = pd.DataFrame(data)
print(df)

print('-----------brand Maruti')
# selecting cars with brand 'Maruti' and Mileage > 25 
print(data.loc[(data.Brand == 'Maruti') & (data.Mileage > 25)]) 
print('-----------0th, 2nd, 4th, and 7th index rows')
# selecting 0th, 2nd, 4th, and 7th index rows 
print(data.iloc[[0, 2, 4, 7]]) 
print('-----------rows from 1 to 4 and columns from 2 to 4')
# selecting rows from 1 to 4 and columns from 2 to 4 
print(data.iloc[1: 5, 2: 5]) 




