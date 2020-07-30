from csv import reader 
from math import sqrt
import matplotlib.pyplot as mpt

#matplotlib labels axes as x1 and x2 values
mpt.xlabel('x1')
mpt.ylabel('x2')



def get_data(percent):
    #data array holds values of co-ordinates in .csv files
    data = []
    #csv_reader used to make gathering data from csv files easy via reader object
    with open('./dataset/datasetQ1.csv', 'r') as obj:
        csv_reader = reader(obj)
        line = next(csv_reader)#skip header line
        if line != None:#if file is not empty
            for row in csv_reader:
                if row[2] == '1':#if y is 1, plot as red circle
                    mpt.plot([row[0]], [row[1]], 'ro')
                else:#otherwise it is 0, plot as blue circle
                    mpt.plot([row[0]], [row[1]], 'bo')
                data.append(row)#after plotting, add the vaalue to data
    obj.close()
    #now we use length to cut off a percentage of the data
    length = len(data)
    length = int(length * (percent * 0.01))
    data = data[:length]
    data = sorted(data)
    mpt.show()
    mpt.clf()
    return data

def fnKNN(data, p, k):
    distances = []#array that holds euclidean distances, in same indices as data array
    for point in data:
        ed = sqrt((float(point[0]) - p[0])**2 + (float(point[1]) - p[1])**2)
        distances.append(ed)

    i=0
    j=1
    selected = []#array that holds the points selected as closest
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
        if elem[2] == '1':#more selected points are red
            reds+=1
        else:#more selected points are blue
            blues+=1

    if reds > blues:
        point  = [str(p[0]), str(p[1]), '1']
    else:
        point  = [str(p[0]), str(p[1]), '0']
    data.append(point)
    data = sorted(data)#sort array after entering new point
    return data

def main():
    p_x1 = float(input("enter x1 for the point: "))
    p_x2 = float(input("enter x2 for the point: "))
    k = int(input("enter the value of k: "))
    percent = int(input("enter percent of data to consider: "))

    p = (p_x1, p_x2)
    data = get_data(percent)

    dataset = fnKNN(data, p, k)
    for row in dataset:
        if row[2] == '1':
            mpt.plot([row[0]], [row[1]], 'ro')
        else:
            mpt.plot([row[0]], [row[1]], 'bo')

    mpt.show()

if __name__ == '__main__': 
    main()