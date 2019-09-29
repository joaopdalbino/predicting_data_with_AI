import unidecode
import pandas as pd
import numpy as np
import os
import csv
import time
import sys 
import xlrd
from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering

file_social_data = '../data/social/PIBMunicipal_2010.csv'
df1 = pd.read_csv(file_social_data, delimiter=';', decimal=',', encoding='utf-8')

print df1['CITY']

df2 = pd.read_csv(file_social_data, delimiter=';', decimal=',', encoding='utf-8')
dolar = 3.96
high_gdp = 12235
low_gdp = 3955

def remove_columns(df):
	del df['PRICES']
	del df['PER CAPITA']
	return df

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

	df_GDP = remove_columns(df_GDP)

	df_GDP.to_csv('../data/scored_GDP.csv', decimal=',', sep=';', encoding='utf-8')

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

	df = remove_columns(df)

	df.to_csv('../data/scored_KMEANS.csv', decimal=',', sep=';', encoding='utf-8')

if __name__ == '__main__':
	
	# bibliograph: 
	#	http://www.ipea.gov.br/ipeageo/bases.html
	#	ftp://ftp.ibge.gov.br/Pib_Municipios/2010_2013/xls/
	#	used class
	#	https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_de_S%C3%A3o_Paulo_por_IDH-M

	df1 = formatting_data(df1)

	scorer_GDP(df1)

	df2 = formatting_data(df2)

	scorer_kmeans(df2)