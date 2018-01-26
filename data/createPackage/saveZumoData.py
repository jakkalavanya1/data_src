'''
Created on 26-Jan-2018

@author: LAVANYA
'''
import numpy as np
import matplotlib.pyplot as plt
import csv
from itertools import zip_longest
filename = 'F:/UNIVERSITY OF DELAWARE/lab/line following/TZ6.csv'
reader = csv.reader(open(filename))
datMat = list(reader) #list of lists is the output
entries = len(datMat)
time = []
for row in datMat:
    if row[1]=='6':
        time.append(row[0])
#print(time)
index = []
for row in datMat:
    if row[1]=='6':
        index.append(row[1])
velocity = []
for row in datMat:
    if row[1] == '6':
        velocity.append(row[4])
#print(index)
d = [time, index,velocity ]
export_data = zip_longest(*d, fillvalue = '')
with  open('C:/Users/LAVANYA/Desktop/sampledata1.csv','w') as newFile:
    writer = csv.writer(newFile)
#    writer.writerow(list1)
    #for i in time:
        #writer.writerow([i])
    writer.writerow(("time", "index","velocity"))
    writer.writerows(export_data)
newFile.close()