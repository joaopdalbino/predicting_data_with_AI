wd <- getwd()
setwd(wd)

df <- read.csv("results/accuracy_validation_KMEANS.csv")
df_uniq <- unique(df)
count(df_uniq)

sum(!duplicated(df$CITY))
425/645