#import relevant packages
import csv as csv
import numpy as np 
#import csv file

csv_file_object = csv.reader(open("../Titanic.csv", 'rb'))

#escape first line which is header line
header = csv_file_object.next()
header[0] = "Id"

#create variable data
data = []

#add each row wrom csv to data

for row in csv_file_object:
	data.append(row)
#convert a data list to array 
data = np.array(data)