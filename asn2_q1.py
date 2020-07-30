from csv import reader 
from math import sqrt
import matplotlib.pyplot as mpt

mpt.xlabel('x1')
mpt.ylabel('x2')

data = []

with open('./dataset/datasetQ1.csv', 'r') as obj:
    csv_reader = reader(obj)
    line = next(csv_reader)
    if line != None:
        for row in csv_reader:
            if row[2] == '1':
                mpt.plot([row[0]], [row[1]], 'ro')
            else:
                mpt.plot([row[0]], [row[1]], 'bo')
            data.append(row)
obj.close()
mpt.show()
mpt.clf()

def fnKNN(data, p, k):
    distances = []
    for point in data:
        ed = sqrt((float(point[0]) - p[0])**2 + (float(point[1]) - p[1])**2)
        distances.append(ed)

    i=0
    j=1
    selected = []
    min = distances[0]
    ref = 0
    while(i<k):
        while(j<len(distances)):
            if distances[j] < min and data[j] not in selected:
                min = distances[j]
                ref = j
            j+=1
        selected.append(data[ref])
        i+=1

    reds = 0
    blues = 0

    for elem in selected:
        if elem[2] == '1':
            reds+=1
        else:
            blues+=1

    if reds > blues:
        point  = [str(p[0]), str(p[1]), '1']
    else:
        point  = [str(p[0]), str(p[1]), '0']
    data.append(point)
    return data

def main():
    p = (1.90, 1.00)
    k = 3

    dataset = fnKNN(data, p, k)
    dataset = sorted(dataset)
    for row in dataset:
        if row[2] == '1':
            mpt.plot([row[0]], [row[1]], 'ro')
        elif row[2] == '0':
            mpt.plot([row[0]], [row[1]], 'bo')
        else:
            mpt.plot([row[0]], [row[1]], 'go')

    mpt.show()

if __name__ == '__main__': 
    main()