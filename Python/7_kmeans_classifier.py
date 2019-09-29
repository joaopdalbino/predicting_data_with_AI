import numpy as np
from sklearn.svm import SVC
import pandas as pd
import csv
from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering

file = '../data/satellites/CSV/F18/2010/2_cs_geo_data_F18_2010.csv'
path_to_save = '../data/'

df = pd.read_csv(file,sep='\t', encoding='utf-8')

def formatting_data(df):
	df['CITY'] = df['CITY'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
	df['CITY'] = map(lambda x: str(x).upper(), df['CITY'])
	return df

def get_array_by_city_name(city_name, df):

	df_partioned = df.loc[df['CITY'] == city_name]

	df_partioned = df_partioned.iloc[[0]]

	array = []

	for i in range(1, 199):
		'P_'+str(i)
		value = df_partioned.iloc[0]['P_'+str(i)]
		array.append(value)

	return array

def get_array(index, df):

	array = []

	for i in range(1, 199):
		'P_'+str(i)
		value = df.at[index, 'P_'+str(i)]
		array.append(value)

	return array

def get_city_name(df):

	file_to_be_saved = path_to_save+'scored_KMEANS.csv'

	i = 0

	X = []
	data_length = len(df)
	for index, row in df.iterrows():
		i+=1
		city_name = row['CITY']
		data = get_array_by_city_name(city_name, df)
		print 'Loading = '+str(i)+' of '+str(data_length)
		X.append(data)

	X = np.reshape(X, (i,198))

	kmeans = KMeans(n_clusters=3)
	kmeans.fit(X)

	y_kmeans = kmeans.predict(X)
	y_kmeans = y_kmeans.reshape(-1, 1)

	df2 = pd.DataFrame(y_kmeans, columns=['CLASS']) 
	for index, row in df2.iterrows():
		df2.set_value(index,'CLASS',row['CLASS']+1)

	df = df.join(df2)

	df[['CITY', 'CLASS']].to_csv('../data/scored_KMEANS.csv', decimal=',', sep=';', encoding='utf-8')

if __name__ == '__main__':

	df = formatting_data(df)

	get_city_name(df)