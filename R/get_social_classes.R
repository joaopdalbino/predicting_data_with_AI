wd <- getwd()
setwd(wd)

df <- read.csv("data/social/ipeadata/income - 1991 until 2000.csv")

min <- df[min(df[,"X2000"], na.rm=T), "City.Name"]

max <- df[max(df[,"X2000"], na.rm=T), "City.Name"]
