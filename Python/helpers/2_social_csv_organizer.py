import pandas as pd
import os
import csv
import time
import sys 
import xlrd
from sklearn.cluster import KMeans

file_social_data = '../../data/social/PIBMunicipal_2010.csv'
df_social = pd.read_csv(file_social_data, delimiter=';', decimal=',')
dolar = 3.97
high_gdp = 16000
low_gdp = 4000

def remove_accents(a):
    return unidecode.unidecode(a.decode('utf-8'))

def formatting_data(df):
	df['CITY'] = df['CITY'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
	df['CITY'] = map(lambda x: str(x).upper(), df['CITY'])
	return df

def scorer_GDP(df_GDP):
	df_GDP['CLASS'] = ''
	for index, row in df_GDP.iterrows():
		per_capita = row['PER CAPITA']
		if per_capita >= (dolar*high_gdp):
			df_GDP.set_value(index,'CLASS',3)
		elif per_capita > (dolar*low_gdp) and per_capita < (dolar*high_gdp): 
			df_GDP.set_value(index,'CLASS',2)
		else:
			df_GDP.set_value(index,'CLASS',1)

	df_GDP.to_csv('../../data/scored_GDP.csv', decimal=',', sep=';', encoding='utf-8')

def scorer_kmeans(df):
	X = df['PER CAPITA'].values
	X = X.reshape(-1, 1)

	kmeans = KMeans(n_clusters=3)
	kmeans.fit(X)
	y_kmeans = kmeans.predict(X)
	y_kmeans = y_kmeans.reshape(-1, 1)
	df2 = pd.DataFrame(y_kmeans, columns=['CLASS']) 
	for index, row in df2.iterrows():
		df2.set_value(index,'CLASS',row['CLASS']+1)

	df = df.join(df2)

	df.to_csv('../../data/scored_KMMEANS.csv', decimal=',', sep=';', encoding='utf-8')

if __name__ == '__main__':
	
	# bibliograph: 
	#	http://www.ipea.gov.br/ipeageo/bases.html
	#	ftp://ftp.ibge.gov.br/Pib_Municipios/2010_2013/xls/
	#	used class
	#	https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_de_S%C3%A3o_Paulo_por_IDH-M

	df_social = formatting_data(df_social)

	scorer_GDP(df_social)

	# scorer_kmeans(df_social)