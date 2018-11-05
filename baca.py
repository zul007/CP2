import csv
with open('tugasspk.csv','r') as filecsv:
    datafile = csv.reader(filecsv)
    for data in  datafile:
       print(data)
