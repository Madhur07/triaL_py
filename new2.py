import pandas as pd
import warnings

warnings.filterwarnings("ignore")

file_path = "C:\\Users\\adity\\Desktop\\DQ\\"

print("Loading latest 13F holdings file")
df = pd.read_csv(file_path+'Data - 13F Appended Final.csv')

# Checking for the Duplicates and Removing them in the Appended Dataset using the column 'Duplicates_checkeD'
# df.drop_duplicates(subset = ['Duplicates_checkeD']).shape  # shape of data after duplicates removal

newdf = df.drop_duplicates(subset=['Duplicates_checkeD'])  # New dataframe after duplicate data removal
print('shape of new dataframe(considering duplicates_check field): ', newdf.shape)
print('shape of previous dataframe: ', df.shape)

print('before removal of duplicates no. of duplicates in df: ', df.duplicated(subset='Duplicates_checkeD').sum())
print('no. of duplicates in newdf_dataframe : ', newdf.duplicated(subset='Duplicates_checkeD').sum())

new2 = newdf.drop_duplicates(subset=['Duplicates_checkeD'])
print('no. of duplicates in new2_dataframe : ', new2.duplicated(subset='Duplicates_checkeD').sum())
print('shape1: ', df.shape)
print('shape2: ', newdf.shape)
print('shape3: ', new2.shape)
