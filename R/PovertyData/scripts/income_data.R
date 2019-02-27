#set source dir
wd <- getwd()
setwd(wd)

#install libs
install.packages("sf")
install.packages("data.table")
install.packages("readxl")

#use libs
library("sf")
library("data.table")
library("readxl")

#read basic csv
data_basic <- read.csv("data/cities_data.csv")

#read income data
data_income <- read_xls("data/ipeadata/Renda per capita - 1991 a 2000.xls")

#clean collumns
data_income$Sigla <- NULL
colnames(data_income)[1] <- 'UF.Code'
colnames(data_income)[2] <- 'City Name'

data_income$UF.Code <- as.integer(data_income$UF.Code)

#create data tables to merge
dt1 <- data.table(data_basic, key = "UF.Code") 
dt2 <- data.table(data_income, key = "UF.Code")

#Join data
data <- dt1[dt2]

#Generates csv file
write.csv(data, file = paste(wd,"/data/ipeadata/", "income - 1991 until 2000.csv", sep = ""))
