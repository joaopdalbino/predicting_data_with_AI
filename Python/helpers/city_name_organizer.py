import pandas as pd
import csv
import xlrd
import numpy as np

file_df1 = '../../results/accuracy_validation_GDP.csv'
df1 = pd.read_csv(file_df1, delimiter=';', decimal=',')
file_df2 = '../../data/city_code.csv'
df2 = pd.read_csv(file_df2, decimal=',', sep=';', encoding='utf-8')

def formatter(df1, df2):
	df1['CITY_CODE'] = None
	for index, row in df1.iterrows():
		r = df2.loc[row['CITY'] == df2['CITY']]
		if len((r['CODE']).values) > 0:
			df1.set_value(index,'CITY_CODE',int((r['CODE']).values))

	df1.to_csv('../../results/accuracy_validation_GDP.csv',  decimal=',', sep=';', encoding='utf-8')

if __name__ == '__main__':

	formatter(df1, df2)