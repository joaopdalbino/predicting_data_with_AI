import pandas as pd
import os
import csv
import time
import sys 
import xlrd

file_social_data = '../../data/social/municipios_atlas_2010.csv'
df = pd.read_csv(file_social_data, delimiter=';', decimal=',')


def scorer(df):
	df['SCORE'] = ''
	for index, row in df.iterrows():
		hdi = row['HDI']
		if hdi >= 0.8 and hdi <= 1:
			df.set_value(index,'SCORE',1)
		elif hdi >= 0.7 and hdi < 0.8: 
			df.set_value(index,'SCORE',2)
		else:
			df.set_value(index,'SCORE',3)

	return df

def organizer(file):
	file = file.loc[file['ANO'] == 2010]
	file = file.loc[file['UF'] == 35]
	file = file[['Munic\xc3\xadpio', 'IDHM']].copy()
	return file.rename(index=str, columns={'Munic\xc3\xadpio': 'CITY', 'IDHM': 'HDI'})

if __name__ == '__main__':
	
	# bibliograph: 
	#	http://www.ipea.gov.br/ipeageo/bases.html
	#	https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_de_S%C3%A3o_Paulo_por_IDH-M

	df = organizer(df)
	df = scorer(df)
	df.to_csv('../../data/hdi_atlas_2010.csv', decimal=',', sep=';', encoding='utf-8')