import pandas as pd
import csv
import xlrd
import numpy as np

file_df1 = '../../data/scored_GDP.csv'
df1 = pd.read_csv(file_df1, delimiter=';', decimal=',')
file_df2 = '../../data/ipea.csv'
df2 = pd.read_csv(file_df2, decimal=',', sep=';', encoding='utf-8')

def remove_accents(a):
    return unidecode.unidecode(a.decode('utf-8'))

def formatting_data(df):
	df['CITY'] = df['CITY'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
	df['CITY'] = map(lambda x: str(x).upper(), df['CITY'])
	return df

def accuracy_maker(df1, df2):
	columns = ['CITY', 'CODE']
	data = []
	cont = 0
	file_name = '../../data/city_code'
	for index, row in df2.iterrows():
		r = df1.loc[df1['CITY'] == row['CITY']]
		if len((r['CLASS']).values) > 0:
			data = [row['CITY'], row['Codigo']]
			print data
			if cont == 0:
				with open(file_name+'.csv', 'wb') as csvfile:
					writer = csv.writer(csvfile, delimiter=';',quotechar='|', quoting=csv.QUOTE_MINIMAL)
					writer.writerow(columns)
					writer.writerow(data)
			else:
				with open(file_name+'.csv', 'a+') as csvfile:
					writer = csv.writer(csvfile, delimiter=';',quotechar='|', quoting=csv.QUOTE_MINIMAL)
					writer.writerow(data)
			cont += 1

if __name__ == '__main__':

	df2 = formatting_data(df2)

	accuracy_maker(df1, df2)