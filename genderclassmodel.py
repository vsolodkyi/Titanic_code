# I create model with the ticket price, class of cabin and passenger's gender
#start 8th of january 2017

import csv as csv
import numpy as np 

csv_file_obj = csv.reader(open('../train.csv', 'rb')) # load train from csv file
header = csv_file_obj.next()						  # escape first line
data = []											  # create variable for data

# add each row fron csv_obj to data
for row in csv_file_obj:
	data.append(row)
data = np.array(data) 								# convert from a list to an array

# then we must bin up data
# add a ceiling
fare_ceiling = 40
# modify fare: if fare > 40 then 39 else fare
data[ data[::, 9].astype(np.float) >= fare_ceiling, 9 ] = fare_ceiling - 1.0
fare_backet_size = 10
number_of_price_brackets = fare_ceiling / fare_backet_size

number_of_classes = 3 								# we know that

number_of_classes_new = len(np.unique(data[0::,2]))	#but much more practice to calculate this

# The reference matrix presetns the proportion of survivors as a sorted table of gender, class and ticket fare
#first we need to initialize it with zeros
survival_table = np.zeros([2, number_of_classes_new, number_of_price_brackets], float)

print (survival_table)
#csv_file_obj.close()

#lets find the stats of all women and men on board
