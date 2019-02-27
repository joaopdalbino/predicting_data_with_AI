#set source dir
wd <- getwd()
setwd(wd)

#install libs
install.packages("sf")
install.packages("readxl")

#use libs
library("sf")
library("readxl")

#read basic csv
cities_data <- read_excel("data/cities_lat_lon.xlsx")

MaxLat <- max(cities_data$MaxLat)
MaxLng <- max(cities_data$MaxLon)
MinLat <- min(cities_data$MinLat)
MinLng <- min(cities_data$MinLon)