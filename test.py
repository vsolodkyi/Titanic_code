# create first prediction
#import relevant packages
import csv as csv
import numpy as np 

test_file = open('../test.csv', 'rb')
test_file_object =csv.reader(test_file)
header = test_file_object.next()
#print ('header is %s' %header)

pred_file = open('../genderbasemodel.csv', 'wb')
pred_file_object = csv.writer(pred_file)
pred_file_object.writerow(["PassengerId", "Survived"])

#repeat in each row

for row in test_file_object:
	if row[3] == 'female':
		pred_file_object.writerow([row[0],'1'])
	else:
		pred_file_object.writerow([row[0], '0'])
test_file.close()
pred_file.close()


