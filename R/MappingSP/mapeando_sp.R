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
data <- read_excel("data/ipeadata[18-09-2018-08-30].xls")

#convert collum Codigo to numeric
data$Codigo <- as.numeric(as.character(data$Codigo))

#get data about State of Sao Paulo from brazilmaps lib
sao_paulo <- get_brmap(geo = "City", geo.filter = list(State = 35), class = "sf")
sao_paulo <- join_data(sao_paulo, data, by = c("City" = "Codigo"))
plot(sao_paulo["2000"])

#This function gets max and min lat and lon from the State of SP
sao_paulo <- get_brmap(geo = "State", geo.filter = list(State = 35), class = "sf")
ret <- sf::st_coordinates(sao_paulo)
ret <- tibble::as_tibble(ret)
colMax <- function(data) sapply(data, max, na.rm = TRUE)
colMin <- function(data) sapply(data, min, na.rm = TRUE)
max <- colMax(ret)
min <- colMin(ret)


