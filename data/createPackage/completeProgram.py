import numpy as np
import matplotlib.pyplot as plt
import csv
from itertools import zip_longest
filename = 'F:/UNIVERSITY OF DELAWARE/lab/line following/CAV data/sorted_battdata_01_07_18__17_22_01.csv'
reader = csv.reader(open(filename))
datMat = list(reader) #list of lists is the output
entries = len(datMat)
time = []
for row in datMat:
    if row[1]=='22':
        time.append(row[0])
#print(time)
index = []
for row in datMat:
    if row[1]=='22':
        index.append(row[1])
xpos = []
for row in datMat:
    if row[1]=='22':
        xpos.append(row[2])
ypos = []
for row in datMat:
    if row[1]=='22':
        ypos.append(row[3])
velocity = []
for row in datMat:
    if row[1] == '22':
        velocity.append(row[4])
battlev = []
for row in datMat:
    if row[1]=='22':
        battlev.append(row[5])
#print(index)
d = [time, index, xpos, ypos, velocity, battlev]
export_data = zip_longest(*d, fillvalue = '')
with  open('C:/Users/LAVANYA/Desktop/lavanya presentation/CAVSimdata22.csv','w',newline = '') as newFile:
    writer = csv.writer(newFile)
#    writer.writerow(list1)
    #for i in time:
        #writer.writerow([i])
#    writer.writerow(("time", "index","velocity"))
    writer.writerows(export_data)
newFile.close()