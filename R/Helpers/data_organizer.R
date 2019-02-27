# Still in development

#set source dir
wd <- getwd()
setwd(wd)

#install libs
install.packages("sf")
install.packages("readxl")
install.packages("qdap")

#use libs
library("sf")
library("readxl")
library("qdap")

#read basic csv
cities_data <- read.csv("data/social/cities_data.csv")
image_data <- read_excel("data/satellites/satellites-data.xlsx")

#cleaning cities data
cities_data$Coordinates <- gsub("[a-zA-Z log\\( log\\) ]", "", cities_data$Coordinates)

apply(cities_data, 1, function(x) any(x %in% "-50.24"))


