from urllib2 import urlopen
import json
import pandas as pd
import unidecode
import os
import time

owd = os.getcwd()
source_dir = '../data/satellites/CSV/'
path_file_name = None

def goes_to_dir(satellite, year):
	file_dir = source_dir+satellite+'/'+year+'/'
	file_name = 'geo_data_'+satellite+'_'+year
	file = file_dir+file_name+'.csv'
	return [file, file_dir, file_name]

def works_with_csv(satellite, year):

	str_year = str(year)
	file_info = goes_to_dir(satellite, str_year)
	df = pd.read_csv(file_info[0],sep = ' ', delimiter = ';')
	path_file_name = file_info[1]+'2_cs_'+file_info[2]+'.csv'
	df = increments_city_info(df)
	df = df[df.STATE == 'SP']
	save_csv(path_file_name, df)
	path_file_name = None

def loader(cont, num_rows, satellite, year):
	per = round((float(cont)/num_rows)*100,2)
	print ('Loading '+str(per)+'%'+' for sattellite = '+satellite+' and year = '+str(year))

def increments_city_info(df):

	original_df = df

	df['CITY'] = ''
	df['STATE'] = ''

	total = len(df.index)
	cont = 0

	for index, row in df.iterrows():
		lat = row['LAT']
		lon = row['LONG']
		sat = row['SATELLITE']

		try:
			array = gets_city_and_state_names(str(lat), str(lon))
		except:
			print 'Error'
			time.sleep(60)
			array = gets_city_and_state_names(str(lat), str(lon))

		if(array[0] is not None):
			df.set_value(index,'CITY',unidecode.unidecode(array[0]))
		else:
			df.set_value(index,'CITY','Erro')

		if(array[1] is not None):
			df.set_value(index,'STATE',unidecode.unidecode(array[1]))
		else:
			df.set_value(index,'STATE','Erro')

		cont += 1
		loader(cont, total,row['SATELLITE'],row['YEAR']) 

	return df

def save_csv(file_name, file):
	file.to_csv(file_name, sep='\t', encoding='utf-8')

def gets_city_and_state_names(lat, lon):
    url = "https://maps.googleapis.com/maps/api/geocode/json?"
    url += "latlng=%s,%s&sensor=false" % (lat, lon)
    url += "&key=PUT_YOUR_API"
    v = urlopen(url).read()
    j = json.loads(v)
    try: 
    	components = j['results'][0]['address_components']
    except:
    	return "Erro"
    country = town = None
    for c in components:
        if "administrative_area_level_2" in c['types']:
            town = c['long_name']
        if "administrative_area_level_1" in c['types']:
            state = c['short_name']
    return [town, state]

if __name__ == '__main__':

	satellites = ['F10', 'F12', 'F14', 'F15', 'F16', 'F18']
	years_range = []

	for sat in satellites:
		
		# if sat == 'F10':
		# 	for n in range(1992, 1995): works_with_csv(sat, n)

		# if sat == 'F12': 
		# 	for n in range(1994, 2000): works_with_csv(sat, n)
		
		# if sat == 'F14': 
		# 	for n in range(1997, 2004): works_with_csv(sat, n)

		if sat == 'F15': 
			for n in range(2007, 2009): works_with_csv(sat, n)

		# if sat == 'F16': 
		# 	for n in range(2004, 2010): works_with_csv(sat, n)

		# if sat == 'F18':
		# 	works_with_csv(sat, 2010)