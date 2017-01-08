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

#print (survival_table)
#csv_file_obj.close()

#lets find the stats of all women and men on board

for i in xrange(number_of_classes_new):
	for j in xrange(number_of_price_brackets):

		women_stats = data[	(data[0::, 4] == "female")\
						&(data[0::,2].astype(np.float) == i+1)\
						&(data[0:,9].astype(np.float) >= j*fare_backet_size)\
						&(data[0:,9].astype(np.float)< (j+1)*fare_backet_size),1]
		men_stats = data[	(data[0::, 4] != "female")\
						&(data[0::,2].astype(np.float) == i+1)\
						&(data[0:,9].astype(np.float) >= j*fare_backet_size)\
						&(data[0:,9].astype(np.float)< (j+1)*fare_backet_size),1]

		survival_table[0,i,j] = np.mean(women_stats.astype(np.float)) # female stats
		survival_table[1,i,j] = np.mean(men_stats.astype(np.float)) 	#male stats

# Since we try to count mean of an array with nothing in it (denominator = 0)
# we convert these to 0
survival_table[ survival_table != survival_table] = 0

# Having my proportion I round them to 0 if survived <0.5 and 1 if >=0.5
survival_table[ survival_table < 0.5] = 0
survival_table[ survival_table >= 0.5] = 1

#print (survival_table)
#print (data[0::, 2])
#print len(data[0])

#Now I can read test file and write out if woman then 1, if men then 0
#first read the test file

test_file = open('../test.csv', 'rb')
test_file_obj = csv.reader(test_file)
header = test_file_obj.next()
print "test_file opens"
# Also I open new file so I can write to it

pred_file = open('../genderclassmodel.csv', 'wb')
pred_file_obj = csv.writer(pred_file)
pred_file_obj.writerow(["PassengerID", "Survived"])
print "pred file creates"
#bin up the price file
for row in test_file_obj:
	for j in xrange(number_of_price_brackets):
		#if there no fare then place of the ticket according to its class ClassName(object):
		try:
			row[8] = float(row[8])
		except:
			bin_fare = 3 - float(row[1])
			break						#break the loop and go to the next row
		if row[8] > fare_ceiling:
			bin_fare = number_of_classes_new - 1
			break
		if row[8] >= j*fare_backet_size\
			and row[8] < (j+1)*fare_backet_size:
			bin_fare = j
			break 	# pass the loop until find appropriate bin then break and move to the next row
	#now we have the binned fare , passenger class, sex - we can 
	# cross with our survival table
	if row[3] == 'female':
		pred_file_obj.writerow([row[0], "%d" % int(survival_table[ 0, float(row[1])-1, bin_fare ])])
	else:
		pred_file_obj.writerow([row[0], "%d" % int(survival_table[1, float(row[1]) - 1, bin_fare ])])

#close our files
print (survival_table)
test_file.close()
pred_file.close()

				