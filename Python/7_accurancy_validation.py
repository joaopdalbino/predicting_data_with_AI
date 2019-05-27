import pandas as pd
import csv
import unidecode

file_social_data = '../data/hdi_atlas_2010.csv'
file_classification_data = '../data/classification.csv'
df_social_data = pd.read_csv(file_social_data, delimiter=';',quotechar='|', decimal=',')
df_class_data = pd.read_csv(file_classification_data, delimiter=';',quotechar='|')

def remove_accents(a):
    return unidecode.unidecode(a.decode('utf-8'))

def formatting_data(df):
	df['CITY'] = df['CITY'].apply(remove_accents)
	return df

def binder(df1, df2):
	for index, row in df2.iterrows():
		print df1.loc[df1['CITY'] == row['CITY']]

if __name__ == '__main__':

	print list(df_social_data)
	# df_social_data = formatting_data(df_social_data)
	# df_class_data = formatting_data(df_class_data)

	# df = binder(df_social_data, df_class_data)