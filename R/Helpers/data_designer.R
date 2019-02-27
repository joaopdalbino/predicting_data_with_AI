# Still in development

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
data_basic <- read.csv("data/cities_data.csv")

csv_creator <- function(data, file){
  
  join_data(data_basic, data, by = c("City" = "City"))
  
}

#get directoris
data_dir <- paste(wd, "/data/", sep = "")
dirs <- basename(list.dirs(data_dir))
dirs <- dirs [! dirs %in% c(".", "data", "ibge")]

for (dir in dirs) {
  dir_files <- paste(data_dir, dir, sep = "")
  files <- list.files(dir_files)
  for (file in files) {
    data <- read_excel(paste(dir_files, "/", file, sep = ""))
    print(file)
    #csv_creator(data)
  }
}