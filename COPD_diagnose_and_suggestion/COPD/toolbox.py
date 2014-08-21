##coding=utf-8
##By Sanhe    2014-6-5
import csv
data = [[1,2],[3,4]]
with open('eggs.csv', 'wb') as f:
    writer = csv.writer(f, delimiter=',')
    for row in data:
        writer.writerow(row)
        
with open('eggs.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=',')
    next(reader, None)
    for row in reader:
        print row
        
        