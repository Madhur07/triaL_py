import pandas as pd
import warnings

warnings.filterwarnings("ignore")

file_path = "C:\\Users\\adity\\Desktop\\DQ\\"

print("Loading latest 13F holdings file")
d1 = pd.read_csv(file_path+'Data - 13F Holdings.csv')

print("Loading backfill 13F holdings file")
d2 = pd.read_csv(file_path+'Data - Backfill 13F Holdings.csv')

# d1.head()
# d2.head()
# print(d1.dtypes)

# Converting the format to DateTime for the Column: 'FILED AS OF DATE', for both the Tables.
d1['FILED AS OF DATE'] = pd.to_datetime(d1['FILED AS OF DATE'], errors='coerce')
d2['FILED AS OF DATE'] = pd.to_datetime(d2['FILED AS OF DATE'], errors='coerce')

# Appending/Concatenating both tables after performing correction.
# Appending the Files as both are corrected for the 'FILED AS OF DATE' field,
# Now as both have similar Fields, so Appending them Directly.

# *Note:  Here Append is also termed as Concatenation, so "Concat" is used.
print("Appending the two files")
df = pd.concat([d1, d2], ignore_index = True )

# Creating a new field "Duplicates_checkeD" Using 'ACCESSION NUMBER' & 'Sr No'
# Here we grouped using both the Columns mentioned above.

print('Grouping 2 fields: ACCESSION Number + Sr No to --> Duplicates_checkeD')
df['Duplicates_checkeD'] = df['ACCESSION NUMBER'].astype(str) + '-' + df['Sr No'].astype(str)
# print(df.head(20))

# Filtering using Dates
df = df[(df['CONFORMED PERIOD OF REPORT'] >= '2018-12-31')]

# Removing Duplicates in the Appended Dataset using the column 'Duplicates_checkeD'
print("Removing duplicates")
newdf = df.drop_duplicates(subset=['Duplicates_checkeD'])  # New dataframe after duplicate data removal
print('shape of new dataframe: ', newdf.shape)
print('shape of previous dataframe: ', df.shape)

# checking duplicates in dataframe using the column 'Duplicates_checkeD' !!
print('no. of duplicates in newdf : ', newdf.duplicated(subset='Duplicates_checkeD').sum())
print('no. of duplicates in df : ', df.duplicated(subset='Duplicates_checkeD').sum())

# For cross-checking duplicate data is removed or not.
print(df[(df['COMPANY CONFORMED NAME'] == '1623 Capital LLC') & (df['Name Of Issuer'] == 'Medtronic Plc')])  ## dataframe with duplicate data
print(newdf[(newdf['COMPANY CONFORMED NAME'] == '1623 Capital LLC') & (newdf['Name Of Issuer'] == 'Medtronic Plc')]) ## dataframe after duplicate data removal

print("Saving output file")
# Saving our cleaned file to new csv.
newdf.to_csv(file_path+'Data - 13F Appended Final.csv', index=False)
print("file saved succesfullY !!")


