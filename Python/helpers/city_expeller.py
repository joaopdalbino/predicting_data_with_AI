from urllib2 import urlopen
import json
import pandas as pd
import unidecode
import os

# Sources: https://stackoverflow.com/questions/20169467/how-to-convert-from-longitude-and-latitude-to-country-or-city

def getplace(lat, lon):
    url = "https://maps.googleapis.com/maps/api/geocode/json?"
    url += "latlng=%s,%s&sensor=false" % (lat, lon)
    url += "&key=PUT_GOOGLE_API_KEY_HERE"
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

def getplacebycity(city):
    url = "https://maps.googleapis.com/maps/api/geocode/json?"
    url += "address=%s,+SP&sensor=true" % (city)
    url += "&key=PUT_GOOGLE_API_KEY_HERE"
    url += "&components=country:BR"
    url += "&components=administrative_area_level_1:SP"

    v = urlopen(url).read()
    j = json.loads(v)
    try: 
    	components = j['results'][0]['geometry']['bounds']
    except:
    	try:
    		components = j['results'][0]['geometry']['viewport']
    	except:
    		return "Erro"

    MaxLat = components['northeast']['lat']
    MaxLong = components['northeast']['lng']
    MinLat = components['southwest']['lat']
    MinLong = components['southwest']['lng']

    array = [MaxLat, MaxLong, MinLat, MinLong]

    return array 

if __name__ == '__main__':

	print 'Select \n 1 - To get a city name giving Lat & Long values \n 2 - To process information from sattelites-data \n 3 - To get max long and min from a city name ';

	user_input = input('Give me a number: ')

	if user_input == 1:
		lat = 1
		lon = 2
		while True:
			lat = input('Give me a lat: ')
			lon = input('Give me a long: ')
			if (lat == 0.0) & (lon == 0.0):
				break
			town = getplace(str(lat), str(lon))
			town = town.encode('utf-8')
			print town

	if user_input == 2:

		df = pd.read_excel('../../data/satellites/satellites-data.xlsx')
		df['City'] = ''
		df['State'] = ''
		total = len(df.index)
		cont = 1

		for index, row in df.iterrows():
			lat = row['LAT']
			lon = row['LONG']
			sat = row['SATELLITE']
			if(lat > -30) & (lon > -60):
				print '\b\r'
				print "lat ="+str(lat)+" || lon = "+str(lon)
				array = getplace(str(lat), str(lon))
				if(array[0] != None):
					df.set_value(index,'City',unidecode.unidecode(array[0]))
					print 'City = '+str(unidecode.unidecode(array[0]))
				else:
					df.set_value(index,'City','Erro')

				if(array[1] != None):
					df.set_value(index,'State',unidecode.unidecode(array[1]))
					print 'State = '+str(unidecode.unidecode(array[1]))
				else:
					df.set_value(index,'State','Erro')
				print '|---  '+str(cont)+'/'+str(total)+' = '+str(cont/total)+' ---|'
				
				cont = cont+1
			# if(row['YEAR'] > 1992):
			# 	break

		df.to_csv('../data/'+sat+'-data.csv', sep='\t', encoding='utf-8')

	if user_input == 3:
		df = pd.read_csv('../data/cities_name.csv')
		df['MaxLat'] = ""
		df['MaxLon'] = ""
		df['MinLat'] = ""
		df['MinLon'] = ""

		for index, row in df.iterrows():
			town = row['cities']
			if " " in town:
				town = town.replace(" ", "%20")
			results = getplacebycity(town)
			df.set_value(index,'MaxLat',results[0])
			df.set_value(index,'MaxLon',results[1])
			df.set_value(index,'MinLat',results[2])
			df.set_value(index,'MinLon',results[3])
			print town

		df.to_csv('cities_lat_lon.csv', sep='\t', encoding='utf-8')