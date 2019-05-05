import urllib
import os
import time

# it defines coordinates latitudes and longitudes from state of sao paulo
MinLong = -52.611579
MinLat = -24.9982777
MaxLong = -44.3304263
MaxLat = -20.0371434

path = "../data/satellites/TIF"
os.chdir(path)

# Creates a path to sabe images
def path_creator(name_path):
	path = os.getcwd() + "/" + name_path
	if not os.path.isdir(path):
	    os.makedirs(path)
	os.chdir(path)

def lat_long_calc(satellite, years_range):
	
	path_creator(satellite)

	for year in years_range:
		
		year = str(year)

		path_creator(satellite+'-'+year)

		done = 0
		cont = 0

		x = MinLong
		y = MaxLat

		#source: https://stackoverflow.com/questions/4000886/gps-coordinates-1km-square-around-a-point
		km_lon = round(10*(360/23903.297),4)
		km_lat = round(10*(360/40075.00),4)

		print "***********"
		print '\n'
		print 'SATELLITE: '+satellite
		print '\n'
		print 'Year: '+year
		print '\n'
		print "***********"

		while done == 0:
			y2 = y - km_lat
			x2 = x + km_lon

			#coordenates
			print '\n'
			print '      '+str(y)
			print ' '+str(x)+'          '+str(x2)
			print '      '+str(y2)
			print '\n'
			cont += 1

			downloadimage(satellite, year, str(x), str(y), str(x2), str(y2))

			if(x2 >= MaxLong):
				if(y2 <= MinLat):
					done = 1
				else:
					x = MinLong
					y = y2
			else:
				x = x2 

		os.chdir("..")
		
	os.chdir("..")

def downloadimage(satellite, year, x, y, x2, y2):
    l = 'b'
    if year == 2010 or 2018:
        l = 'c'
    try:
    	st = satellite+year
    	url = 'https://gis.ngdc.noaa.gov/cgi-bin/public/gcv4/'+st+'.v4'+l+'_web.stable_lights.avg_vis.lzw.tif?request=GetCoverage&service=WCS&version=1.0.0&COVERAGE='+st+'.v4'+l+'_web.stable_lights.avg_vis.lzw.tif&crs=EPSG:4326&format=geotiff&resx=0.0083333333&resy=0.0083333333&bbox='+x+','+y2+','+x2+','+y+''
    	print str(url)
    	file = urllib.URLopener()
    	name_file = satellite+"_"+year+"_"+x+"_"+y+".TIF"
    	if os.path.isfile(path+name_file):
    	    print 'file already exists'
    	else:
    	    file.retrieve(url,name_file)

    except:
    	time.sleep(60)
    	var = [satellite, year, x, y, x2, y]
    	downloadimage(satellite, year, x, y, x2, y2)

if __name__ == '__main__':    

    satellites = ['F10', 'F12', 'F14', 'F15', 'F16', 'F18']

    years_range = []

    #path_creator("data")


    #IMAGE DOWNLOADER
    #Calls functions to download images
    for sat in satellites:

		if sat == 'F10': 
			for n in range(1992, 1995): years_range.append(n)

		if sat == 'F12': 
		 	for n in range(1995, 2000): years_range.append(n)

		if sat == 'F14':
		 	 for n in range(1997, 2004): years_range.append(n)

		if sat == 'F15':
			for n in range(2000, 2009): years_range.append(n)

		if sat == 'F16':
			for n in range(2004, 2010): years_range.append(n)
		
		if sat == 'F18':
			years_range = [2010]

		lat_long_calc(sat, years_range)    
		years_range = []