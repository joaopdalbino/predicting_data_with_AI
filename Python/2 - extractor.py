from PIL import Image
import cv2
import numpy
import os
from os import listdir
from os.path import isfile, join

source_path = '../data/satellites/'
os.chdir(source_path)
source_path = os.getcwd()

destination_path = source_path+'/PGM/'

def path_creator(name_path):
	path = os.getcwd() + "/" + name_path
	if not os.path.isdir(path):
	    os.makedirs(path)
	os.chdir(path)

def path_finder(satellite, years):

	path_creator(satellite)

	for year in years:

		year = str(year)

		path_creator(satellite+'-'+year)

		sat_dir = sat+'/'+sat+'-'+year
		files_path = source_path+'/TIF/'+sat_dir
		os.chdir(files_path)
		files_path = files_path + '/'
		get_files = [f for f in listdir(files_path) if isfile(join(files_path, f))]
		for file in get_files:
			new_file = converter(files_path, file)
			file_name = os.path.splitext(file)[0]
			writer(sat_dir+'/', new_file, file_name)

		os.chdir(destination_path+satellite)

	os.chdir(destination_path)

def writer (path_to_save, file, file_name):

	path_dest = destination_path + path_to_save + file_name + ".pgm"
	
	cv2.imwrite(path_dest,file)

def converter (path_to_img, img_file):

	im = Image.open(path_to_img+img_file)
	
	return numpy.array(im)

if __name__ == '__main__':

	satellites = ['F10', 'F12', 'F14', 'F15', 'F16', 'F18']

	years_range = []

	path_creator("PGM")

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

		path_finder(sat, years_range)
		years_range = []