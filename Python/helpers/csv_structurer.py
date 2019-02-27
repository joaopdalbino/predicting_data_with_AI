import pandas as pd

origin_path = '../data/'

df = pd.read_excel(origin_path+'[final]cities_structured_data.xlsx')

df = df[df.YEAR == 1992]

df.to_excel('../data/[final]data.xlsx')

df = pd.read_excel(origin_path+'[final]data.xlsx')

df = df[df.State == 'SP']

df.to_excel(origin_path+'1992_data.xlsx')