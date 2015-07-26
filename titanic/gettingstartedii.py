import csv as csv
import numpy as np

wdir = '/Users/dwhitehead/Documents/github/kaggle/titanic/'

csv_file_object = csv.reader(open(wdir + 'train.csv', 'rb'))
header = csv_file_object.next()
data = []

for row in csv_file_object:
    data.append(row)
data = np.array(data)

print data[0:15]
