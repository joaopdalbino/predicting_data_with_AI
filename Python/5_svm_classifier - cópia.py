import numpy as np
from sklearn.svm import SVC
import pandas as pd
import csv

file = '../data/satellites/CSV/F18/2010/2_cs_geo_data_F18_2010.csv'

df = pd.read_csv(file,sep='\t', encoding='utf-8')
path_to_save = '../data/'

def remove_accents(a):
    return unidecode.unidecode(a.decode('utf-8'))

def formatting_data(df):
	df['CITY'] = df['CITY'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
	df['CITY'] = map(lambda x: str(x).upper(), df['CITY'])
	return df

def class_definer():

	classes_by_city = ['BARRA DO CHAPEU', 'IRACEMAPOLIS', 'LOUVEIRA']

	X = []

	for city in classes_by_city:
		data = get_array_by_city_name(city, df)
		X.append(data)

	X = np.reshape(X, (3,198))

	# X = X.reshape((1,198))
	y = np.array([1, 2, 3])

	clf = SVC(gamma='scale')

	clf.fit(X, y)

	return clf

def classifier(city_name, clf):

	to_be_predict = []
	to_be_predict = np.asarray(get_array(city_name, df))
	to_be_predict = to_be_predict.reshape((1,198))
	
	class_num = clf.predict(to_be_predict)

	return class_num[0]

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

def get_city_name(df, clf):

	file = path_to_save+'cities_classified_by_svm.csv'

	for index, row in df.iterrows():
		city_name = row['CITY']
		array = get_array(index, df)
		city_class = classifier(index, clf)
		if index == 0:
			with open(file, 'wb') as csvfile:
				writer = csv.writer(csvfile, delimiter=';',quotechar='|', quoting=csv.QUOTE_MINIMAL)
				header = ['CITY', 'CLASS']
				writer.writerow(header)
				writer.writerow([city_name, city_class])
		else:
			with open(file, 'a+') as csvfile:
				writer = csv.writer(csvfile, delimiter=';',quotechar='|', quoting=csv.QUOTE_MINIMAL)
				writer.writerow([city_name, city_class])

if __name__ == '__main__':

	df = formatting_data(df)

	clf = class_definer()

	get_city_name(df, clf)

	# bibliograph: https://towardsdatascience.com/https-medium-com-pupalerushikesh-svm-f4b42800e989
	# Lowest = BARRA DO CHAPEU
	# Mid = IRACEMAPOLIS
	# Higher = LOUVEIRA