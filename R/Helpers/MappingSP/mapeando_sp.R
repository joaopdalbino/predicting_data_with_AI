#set source dir
setwd('/Users/joaopedroalbino/Desktop/PredizendoNiveisdePobreza/Projeto_PredizendoPobrezas/R/Mapeando_Sao_Paulo/Map_SP')

#install libs
install.packages("brazilmaps")
install.packages("WriteXLS")
install.packages("sf")
install.packages("readxl")

#load libs
library(brazilmaps)
library("WriteXLS")
library("sf")
library("readxl")

#extract data from excel
data_basic <- read.csv("results/accuracy_validation_GDP.csv", sep = ';')
data_basic <- read.csv("results/accuracy_validation_KMEANS.csv", sep = ';')

#convert collum Codigo to numeric
data_basic$CITY_CODE <- as.numeric(as.character(data_basic$CITY_CODE))

#get data about State of Sao Paulo from brazilmaps lib
sao_paulo <- get_brmap(geo = "City", geo.filter = list(State = 35), class = "sf")
sao_paulo <- join_data(sao_paulo, data_basic, by = c("City" = "CITY_CODE"))
plot(sao_paulo['GDP'])

#This function gets max and min lat and lon from the State of SP
sao_paulo <- get_brmap(geo = "State", geo.filter = list(State = 35), class = "sf")
ret <- sf::st_coordinates(sao_paulo)
ret <- tibble::as_tibble(ret)
colMax <- function(data) sapply(data, max, na.rm = TRUE)
colMin <- function(data) sapply(data, min, na.rm = TRUE)
max <- colMax(ret)
min <- colMin(ret)


