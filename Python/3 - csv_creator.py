import numpy as np
import os
from PIL import Image
import csv
from os import listdir
from os.path import isfile, join

destination_path = '../data/satellites/PGM/'
os.chdir(destination_path)
destination_path = os.getcwd()

def file_finder(satellite, year):

	for year in years_range:
		year = str(year)

		sat_dir = sat+'/'+sat+'-'+year
		files_path = destination_path+'/'+sat_dir
		files_path = files_path + '/'
		get_files = [f for f in listdir(files_path) if isfile(join(files_path, f))]
		for file in get_files:
			file_name = os.path.splitext(file)[0].split('_');
			new_array = matrix_worker(files_path, file)
			writer(file_name[0], file_name[1], file_name[2],  file_name[3], new_array)

def writer (satellite, year, longi, lat, big_array):
	
	with open('../satellites-data.csv', 'a') as csvfile:
		writer = csv.writer(csvfile, delimiter=';',quotechar='|', quoting=csv.QUOTE_MINIMAL)
		prefix = [satellite, year, longi, lat]
		writer.writerow(np.concatenate((prefix, big_array), axis=None))

	
def matrix_worker (path_to_img, img_file):

	im = Image.open(path_to_img+img_file)
	matrix = np.array(im)

	i = 0

	big_array = []

	while i < int(np.size(matrix, 0)):
		array = matrix[i]
		big_array = np.concatenate((big_array, array), axis=None)
		i += 1
	
	return big_array

def csv_creator():
	with open('../satellites-data.csv', 'wb') as csvfile:
		filewriter = csv.writer(csvfile, delimiter=';',quotechar='|', quoting=csv.QUOTE_MINIMAL)
		header = ['SATELLITE', 'YEAR', 'LONG', 'LAT']
		for i in range(1, 199):
			name_collumn = 'P_'+str(i)
			header.append(name_collumn)
		filewriter.writerow(header)


if __name__ == '__main__':


	csv_creator()
	
	#satellites = ['F10', 'F12', 'F14', 'F15', 'F16', 'F18']

	satellites = ['F10', 'F12', 'F14', 'F15', 'F16']

	years_range = []

	for sat in satellites:
		
		if sat == 'F10':
			for n in range(1992, 1995): years_range.append(n)

		# if sat == 'F12': 
		# 	for n in range(1994, 2000): years_range.append(n)
		
		# if sat == 'F14': 
		# 	for n in range(1997, 2004): years_range.append(n)

		# if sat == 'F15': 
		# 	for n in range(2000, 2009): years_range.append(n)

		# if sat == 'F16': 
		# 	for n in range(2004, 2010): years_range.append(n)

		# if sat == 'F18':
		# 	years_range = [2010]

		file_finder(sat, years_range)
		years_range = []