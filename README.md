# predicting_data_with_AI

## This project aims to develop a AI system capable of predicting poverty rate in the state of Sao Paulo, Brazil

#How to run it?

##Setting up some data
1 - To extract sattelites images from the state of SP run Python/1_colector
2 - Run Python/2_extractor to convert JPG files to PGM
3 - Python/3_csv_creator creates the CSV file of all PGM files
4 - Python/4_city_aggregator to struct data to be analyzed

##Creating some AI
5 - Run 5_svm_classifier that is the SVM classifier to prepare our hipotesis
6 - Run 6_class_makers to create classes based on GDP and Kmeans
7 - Check the results!

#Observations
- Python/helpers has files that helped structure data
