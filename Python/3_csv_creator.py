import numpy as np
import pandas as pd
import os
from os import system, name , listdir
from os.path import isfile, join, expanduser
from PIL import Image
import csv
import time
import sys 

owd = os.getcwd()
source_path = '../data/satellites/CSV/'
images_folder = '../data/satellites/PGM/'

def creates_dir(path):
	if not os.path.isdir(path):
		os.makedirs(path)

def loader(cont, num_files):
	per = round((float(cont)/num_files)*100,2)
	print ('Loading '+str(per)+'%')

def file_finder(satellite, year):

	satellite_folder = source_path+satellite
	creates_dir(satellite_folder)

	for year in years_range:
		year = str(year)
		sat_dir = satellite+'/'+satellite+'-'+year
		files_dir = images_folder+sat_dir+'/'
	 	os.chdir(files_dir)
	 	files_dir = os.getcwd()
		get_files = [f for f in listdir(files_dir) if isfile(join(files_dir, f))]
		num_files = len(get_files)
		cont = 0
		for file in get_files:
			file_name = os.path.splitext(file)[0].split('_');
			new_array = matrix_worker(files_dir, file)
			try:
				writer(file_name[0], file_name[1], file_name[2],  file_name[3], new_array, satellite_folder)
			except:
				print 'Error'
				time.sleep(30)
			cont += 1
			loader(cont, num_files)
		go_back_root_dir()
		cont = 0
	go_back_root_dir()

def go_back_root_dir():
	os.chdir(owd)

def writer (satellite, year, longi, lat, big_array, satellite_folder):

	go_back_root_dir()
	satellite_year_folder = satellite_folder+'/'+year
	creates_dir(satellite_year_folder)
	os.chdir(satellite_year_folder)
	satellite_year_folder = os.getcwd()

	file = satellite_year_folder+'/'+'geo_data_'+sat+'_'+str(year)+'.csv'
	
	if os.path.isfile(file) == False:
		with open(file, 'wb') as csvfile:
			writer = csv.writer(csvfile, delimiter=';',quotechar='|', quoting=csv.QUOTE_MINIMAL)
			header = ['SATELLITE', 'YEAR', 'LONG', 'LAT']
			for i in range(1, 199):
				name_collumn = 'P_'+str(i)
				header.append(name_collumn)
			writer.writerow(header)
	else:
		with open(file, 'a+') as csvfile:
			writer = csv.writer(csvfile, delimiter=';',quotechar='|', quoting=csv.QUOTE_MINIMAL)
			prefix = [satellite, year, longi, lat]
			writer.writerow(np.concatenate((prefix, big_array), axis=None))
	
def matrix_worker (path_to_img, img_file):

	im = Image.open(path_to_img+'/'+img_file)
	matrix = np.array(im)

	i = 0

	big_array = []

	while i < int(np.size(matrix, 0)):
		array = matrix[i]
		big_array = np.concatenate((big_array, array), axis=None)
		i += 1
	
	return big_array

if __name__ == '__main__':
	
	creates_dir(source_path)
	satellites = ['F10', 'F12', 'F14', 'F15', 'F16', 'F18']
	years_range = []

	for sat in satellites:
		
		if sat == 'F10':
			for n in range(1992, 1995): years_range.append(n)

		if sat == 'F12': 
			for n in range(1994, 2000): years_range.append(n)
		
		if sat == 'F14': 
			for n in range(1997, 2004): years_range.append(n)

		if sat == 'F15': 
			for n in range(2000, 2009): years_range.append(n)

		if sat == 'F16': 
			for n in range(2004, 2010): years_range.append(n)

		if sat == 'F18':
			years_range = [2010]

		file_finder(sat, years_range)
		years_range = []