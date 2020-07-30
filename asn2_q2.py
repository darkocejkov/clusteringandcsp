import matplotlib.pyplot as mpt
import numpy as np
from csv import reader 
from math import sqrt

mpt.xlabel('f1')
mpt.ylabel('f2')

data = []
with open('./dataset/datasetQ2.csv', 'r') as obj:
    csv_reader = reader(obj)
    line = next(csv_reader)
    if line != None:
        for row in csv_reader:
            mpt.plot([row[0]], [row[1]], 'bo')
            data.append(row)
obj.close()
mpt.show()
mpt.clf()

def kmeans(data, k):
    