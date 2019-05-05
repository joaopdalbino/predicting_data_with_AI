import numpy as np
from sklearn.svm import SVC
import pandas as pd
import csv
from statistics import mean, median, mode, stdev

file = '../data/classes.csv'
df = pd.read_csv(file, delimiter=';',quotechar='|')
path_to_save = '../data/'

def class_definer():

	X = []

	X = [[1,1,1], [1,1,2], [3,1,1], [2,2,2], [2,2,1], [3,2,2], [3,3,3], [3,3,2], [3,3,2]]

	y = np.array([1, 1, 1, 2, 2, 2, 3, 3, 3])

	clf = SVC(gamma='scale')

	clf.fit(X, y)

	return clf

def classifier(array, clf):
	class_num = clf.predict(array)
	return class_num

def organizer(values):
	try:
		values_mode = float(mode(values))
	except:
		values_mode = values[0]
	total = float(len(values))
	array = []
	mode_participation_1 = values.count(values_mode)/total
	array.append(values_mode)
	if(0.67 <= mode_participation_1 <= 0.8):
		array.append(values_mode)
		values.remove(values_mode)
		try:
			values_mode_2 = float(mode(values))
		except:
			values_mode_2 = array[0]
		array.append(values_mode_2)
		return array
	elif (mode_participation_1 > 0.8):
		for n in range(2): array.append(values_mode)
		return array
	elif (mode_participation_1 < 0.67):
		values.remove(values_mode)
		try:
			values_mode_2 = float(mode(values))
		except:
			values_mode_2 = array[0]
		array.append(values_mode_2)
		mode_participation_2 = values.count(values_mode_2)/total
		values.remove(values_mode_2)
		try:
			values_mode_3 = float(mode(values))
		except:
			values_mode_3 = array[0]
		if(values.count(values_mode_3)/total <= 0.1):
			if(mode_participation_1 > mode_participation_2):
				array.append(values_mode)
			else:
				array.append(values_mode_2)
		else:
			array.append(values_mode_3)
		return array

def get_array_by_city_name(city_name, df):

	df_partioned = df.loc[df['CITY'] == city_name]
	values = list(df_partioned['CLASSES'])
	print values
	array = np.array(organizer(values))
	print array
	return array.reshape(1, -1)

def get_city_classification(city_name, df, index, clf, file):

	array = get_array_by_city_name(city_name, df)
	city_class = classifier(array, clf)

	if index == 0:
		with open(file, 'wb') as csvfile:
			writer = csv.writer(csvfile, delimiter=';',quotechar='|', quoting=csv.QUOTE_MINIMAL)
			header = ['CITY', 'CLASSES', 'CLASS']
			writer.writerow(header)
			writer.writerow([city_name, array, city_class])
	else:
		with open(file, 'a+') as csvfile:
			writer = csv.writer(csvfile, delimiter=';',quotechar='|', quoting=csv.QUOTE_MINIMAL)
			writer.writerow([city_name, array, city_class])

def classify(df, clf):

	file = path_to_save+'classes_edition.csv'
	cities_that_ve_been_checked = []
	for index, row in df.iterrows():
		city_name = row['CITY']
		if city_name not in cities_that_ve_been_checked:
			print city_name
			get_city_classification(city_name, df, index, clf, file)
			cities_that_ve_been_checked.append(city_name)

if __name__ == '__main__':

	clf = class_definer()
	classify(df, clf)