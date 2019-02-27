#set source dir
wd <- getwd()
setwd(wd)

#install libs
install.packages("brazilmaps")
install.packages("sf")
install.packages("readxl")

#use libs
library(brazilmaps)
library("sf")
library("readxl")

#get data about State of Sao Paulo from brazilmaps lib
sao_paulo_data <- get_brmap(geo = "City", geo.filter = list(State = 35), class = "sf")

#creates data frame with column names
header <- c('City','UF Code', 'Microregion', 'Mesoregion', 'Coordinates')
cities <- sao_paulo_data$nome
#ufcode <- sao_paulo_data$City
#micro <- sao_paulo_data$MicroRegion
#meso <- sao_paulo_data$MesoRegion
#coordinates <- sao_paulo_data$geometry
#coordinates <- vapply(sao_paulo_data$geometry, paste, collapse = ", ", character(1L))
#df <- as.data.frame(cbind(toString(cities), ufcode, micro, meso, coordinates))
df <- as.data.frame(cities)
names(df) <- header

#creates csv
write.csv(df, file = paste(wd,"/data/", "cities_name.csv", sep = ""))





