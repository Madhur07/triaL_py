import pandas as pd

file_path = "C:\\Users\\mmadh\\Videos\\Business Quant\\Day_4\\"
print('Loading csv file...')
df1 = pd.read_csv(file_path+'Unpivoted File.csv', low_memory=False)

# Creating new dataframe with needed columns
print('Creating new data frame with needed columns..')
df2 = df1[['Industry', 'dimension', 'Category', 'Value']]

# Grouping accordingly
print("Grouping by columns: 'Industry', 'Dimention' and 'Category' and also calculating the Median using the column 'Value'.")
df3 = df2.groupby(['Industry', 'dimension', 'Category']).Value.agg(['median'])
df3.rename(columns={'median': 'Value'}, inplace =True)
# Adding new column
print('adding isdelisted column to new dataframe with static value "N"...')
df3['isdelimited'] = 'N'

# Saving new csv file with Median Calculation
print('Saving new csv file...')
df3.to_csv(file_path+'filtered_Median.csv')
