#install libs
install.packages("readxl")
library("readxl")

#reads cities data
cities_data <- read_excel("data/cities_with_data.xlsx")
data <- cities_data
#cleaning rows
data$SATELLITE <- NULL
data$YEAR <- NULL
data$LONG <- NULL
data$LAT <- NULL
data$City <- NULL
data$Means <- NULL

#setting data frame for analysis
data<- sapply( data, as.numeric )
data <- data.frame(ID=data[,1], Means=rowMeans(  data[,-1] ))
datameans <- data
means <- mean(data$Means)
med <- median(data$Means)
mode <- subset(data,data==max(data))
var <- var(data$Means)
dev <- sd(data$Means)

#histogram
hist(data$Means, 
     main="Classes", 
     xlab="Pixels Means", 
     border="blue", 
     col="blue",
     las=1)

####SETTING RANGES
range1 <- sum(data$Means < 0.1)
range2 <- sum((data$Means >= 0.1)&(data$Means < 4))
range3 <- sum(data$Means >= 4)

### CLASSES
# Poor: 0 |- 0.1
# Middle: 0.1 |- 4
# Rich: >= 4