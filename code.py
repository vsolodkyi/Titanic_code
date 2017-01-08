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

#useful functions
number_passengers = np.size(data[0::,0].astype(np.float))
number_survived = np.sum(data[0::,6].astype(np.float))
proportion_survivors = number_survived / number_passengers

#stat functions

women_stats = data[0::,4] == "female"
men_stats = data[0::,4] != "female"
#print women_stats
#print data[women_stats,::]
women_onboard = data[women_stats,-2].astype(np.float)
men_onboard = data[men_stats,-2].astype(np.float)
#print (women_onboard)
proportion_women_survived = \
	np.sum(women_onboard)/np.size(women_onboard)
proportion_men_survived = np.sum(men_onboard)/np.size(men_onboard)

#output proportions 
print ("proportion women survivied is %s"  % proportion_women_survived)

print ("proportion men survivied is %s" % proportion_men_survived)
