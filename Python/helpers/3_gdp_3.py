import pandas as pd
import csv
import xlrd
import numpy as np

file_social_data = '../../data/social/PIBMunicipal_2010.csv'
df = pd.read_csv(file_social_data, delimiter=';', decimal=',')

if __name__ == '__main__':

	df = df.sort_values(by=['PER CAPITA'])

	maxi = df[df['PER CAPITA']==df['PER CAPITA'].max()]
	mini = df[df['PER CAPITA']==df['PER CAPITA'].min()]

	print '1 - Max City: '+str(maxi['CITY'].values)+' by GDP (PIB in Brazil) = '+str(maxi['PER CAPITA'].values)
	print '2 - Min City: '+str(mini['CITY'].values)+' by GDP (PIB in Brazil) = '+str(mini['PER CAPITA'].values)

	mean = sum(df['PER CAPITA']) / len(df) 

	df_sort = df.iloc[(df['PER CAPITA']-mean).abs().argsort()[:1]]

	print df_sort

	print '2 - Mean City: '+str(df_sort['CITY'].values)+' by GDP (PIB in Brazil) = '+str(df_sort['PER CAPITA'].values)