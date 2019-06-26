import pandas as pd
import csv
import xlrd
import numpy as np

file = '../../data/satellites/CSV/F18/2010/2_cs_geo_data_F18_2010.csv'
df = pd.read_csv(file, sep='\t', encoding='utf-8')
df['TOTAL'] = None
df['TOTAL'] = df.iloc[:, -201:-3].sum(axis=1)
df.drop(df.columns.difference(['CITY','TOTAL']), 1, inplace=True)
df = df.groupby(['CITY']).sum(axis=1)
df.to_csv('teste.csv',  decimal=',', sep=';', encoding='utf-8')
maxi = df[df['TOTAL']==df['TOTAL'].max()]
mini = df[df['TOTAL']==df['TOTAL'].min()]
print maxi
print mini

mean = sum(df['TOTAL']) / len(df) 
df_sort = df.iloc[(df['TOTAL']-mean).abs().argsort()[:1]]

print df_sort

# mean = sum(df['TOTAL']) / len(df) 