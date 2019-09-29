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
library(dplyr)
library(stringi)

#extract data from excel
data_basic <- read.csv("data/city_code.csv", sep = ';', )
data_basic$CITY <- stri_enc_mark(data_basic$CITY)

data_basic_svm <- read.csv("results/accuracy_validation_SVM.csv", sep = ';')
group_by(data_basic_svm,CITY)
df1 <- left_join(data_basic_svm, data_basic, by = c("CITY" = "CITY"))


data_basic_KMEANS <- read.csv("results/accuracy_validation_KMEANS.csv", sep = ';')

#convert collum Codigo to numeric
data_basic$CITY_CODE <- as.numeric(as.character(data_basic$CITY_CODE))

#get data about State of Sao Paulo from brazilmaps lib
sao_paulo <- get_brmap(geo = "City", geo.filter = list(State = 35), class = "sf")
sao_paulo <- as.data.frame(sao_paulo)
sao_paulo$nome <-  stri_encode(sao_paulo$nome, "UTF-8", "UTF-8")
sao_paulo <- join_data(sao_paulo, data_basic, by = c("City" = "CODE"))
sao_paulo <- join_data(sao_paulo, data_basic_svm, by = c("CITY" = "CITY"))
sao_paulo <- join_data(sao_paulo, data_basic_KMEANS, by = c("CITY" = "CITY"))
plot(sao_paulo['GDP.y'])
plot(sao_paulo['KMEANS'])
plot(sao_paulo['SVM'])

#This function gets max and min lat and lon from the State of SP
sao_paulo <- get_brmap(geo = "State", geo.filter = list(State = 35), class = "sf")
ret <- sf::st_coordinates(sao_paulo)
ret <- tibble::as_tibble(ret)
colMax <- function(data) sapply(data, max, na.rm = TRUE)
colMin <- function(data) sapply(data, min, na.rm = TRUE)
max <- colMax(ret)
min <- colMin(ret)


