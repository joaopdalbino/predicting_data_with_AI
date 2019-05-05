import pandas as pd
df = pd.read_csv('2_cs_geo_data_F10_1992.csv', sep='\t', encoding='utf-8')
df = df[df.STATE == 'SP']
df.to_csv('2_cs_geo_data_F10_1992.csv', sep='\t', encoding='utf-8')