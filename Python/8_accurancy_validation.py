import pandas as pd
import csv
import unidecode
import re

file_classification_data = '../data/scored_GDP.csv'
df_GDP = pd.read_csv(file_classification_data, delimiter=';',quotechar='|')

def remove_accents(a):
    return unidecode.unidecode(a.decode('utf-8'))

def formatting_data(df):
	df['CITY'] = df['CITY'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
	df['CITY'] = map(lambda x: str(x).upper(), df['CITY'])
	return df

def binder(classified_df, gdp_df, indicator):

	columns = ['INDEX', 'CITY', indicator, 'GDP', 'ACCURACY']
	data = []
	cont = 0
	cont_ac = 0
	file_name = '../results/accuracy_validation_'+indicator
	for index, row in classified_df.iterrows():
		r = gdp_df.loc[gdp_df['CITY'] == row['CITY']]
		if len((r['CLASS']).values) > 0:
			if len((r['CLASS']).values) > 0:
				v = int((r['CLASS']).values)
			print r['CLASS'].values
			# c = int(re.search(r'\d+',row['CLASS']).group())
			c = row['CLASS']
			if v == c:
				accuracy = 1
				cont_ac += 1
			else:
				accuracy = 0
			data = [cont, row['CITY'], v, c, accuracy]
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

	ac = round((float(cont_ac)/float(cont))*100,2)

	data = [cont, 'RESULT', cont_ac, cont, str(float(ac))+'%']
	with open(file_name+'.csv', 'a+') as csvfile:
		writer = csv.writer(csvfile, delimiter=';',quotechar='|', quoting=csv.QUOTE_MINIMAL)
		writer.writerow(data)
	
	print 'Accuracy = '+str(ac)+'%'

if __name__ == '__main__':

	indicators = ['SVM', 'KMEANS']

	for indicator in indicators:

		filename_social = '../data/scored_'+indicator+'.csv'
		df_classfied = pd.read_csv(filename_social, delimiter=';', decimal=',')

		df_classfied = formatting_data(df_classfied)
		df_GDP = formatting_data(df_GDP)

		df = binder(df_classfied, df_GDP, indicator)