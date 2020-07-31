import matplotlib.pyplot as mpt
import numpy as np
from csv import reader 
from math import sqrt
from copy import deepcopy

mpt.xlabel('f1')
mpt.ylabel('f2')

def plot_data(fn, arr=None, k=0, centroid=None):
    data = []
    if arr == None:
        with open(fn, 'r') as obj:
            csv_reader = reader(obj)
            line = next(csv_reader)
            if line != None:
                for row in csv_reader:
                    mpt.plot(row[0], row[1], 'bo')
                    data.append(row)
        obj.close()  
    else:
        #mpt.ylim(top=100)
        #mpt.xlim(right=100)
        colors = [
            'b',
            'r',
            'g',
            'c',
            'y',
            'k',
            'w',
        ]
        #print(centroid[0][0])
        i = 31
        j = 67
        print(f"{i} {j}")
        #mpt.plot(i, j, colors[0]+"*")
        for x in range(k):
            cluster = arr[x]
            #color_choice = ""
            #color_choice = colors[x]+"o"
            cluster[x].append(centroid[x])
            #mpt.plot(centroid[x][0], centroid[x][1], colors[x]+"*")
            for y in range(len(cluster)):
                mpt.plot(cluster[y][0], cluster[y][1], colors[x]+"o")

                #SORT ARRAY LMAOOO

    mpt.show()
    mpt.clf()

    return data

def euclid_dist(p1, p2):
    return round(sqrt((int(p1[0]) - int(p2[0]))**2 + (int(p1[1]) - int(p2[1]))**2), 3)
    
def min_index(arr):
    mx = arr[0]
    min_index = 0
    c = 0
    for x in arr:
        if(x < mx):
            mx = x
            min_index = c
        c += 1

    return min_index

def kmeans(data, k):
    centroids = []
    for x in range(k):
        centroids.append(data.pop(0)) #take first k points as centroids

    print(data)
    print(f"centroids: {centroids}")
    
    cluster_data = []
    for x in range(k):
        cluster = []
        cluster_data.append(cluster)

    old_centroids = []

    converge = False
    c = 0
    while(not converge):
        print(f"RUN {c+1}")
        idx = 0
        for datum in data:
            dist = []
            for x in range(k): #calc euclidean dist. from a point to ALL centroids
                dist.append(euclid_dist(datum, centroids[x])) 

            closest_cluster_idx = min_index(dist)
            local_cluster = cluster_data[closest_cluster_idx] 
            
            
            for x in range(k): #assign
                if(x != closest_cluster_idx):
                    if(datum in cluster_data[x]):
                        cluster_data[x].remove(datum)
                else:
                    if(datum not in local_cluster):
                        local_cluster.append(datum) #put 

            idx += 1

        #once all points have been sorted into their respective cluster, put initial centroids back (only for first run)
        if(c == 0):
            for x in range(k):
                cluster_data[x].append(centroids[x])
            c += 1

        #centroids = [[],[]]
        old_centroids = deepcopy(centroids)
        print(f"old: {old_centroids}; new: {centroids}")
        #print(f"after assignment 0: {cluster_data[0]}")
        #print(f"after assignment 1: {cluster_data[1]}")
        #print(f"centroids: {centroids}")

        #now we must calculate the new centroids
        for x in range(k):
            local_cluster = cluster_data[x]
            i = 0
            j = 0
            length = len(local_cluster)
            for y in range(length):
                i += int(local_cluster[y][0])
                j += int(local_cluster[y][1])
            print(f"{x} i: {i}; j: {j}; len: {length}")
            i = round(i/length, 3)
            j = round(j/length, 3)
            print(f"{x} i: {i}; j: {j}")
            new_centroid = [i,j]
            centroids[x] = new_centroid

        print(f"old: {old_centroids}; new: {centroids}")
        if(centroids == old_centroids):
            converge = True
        else:
            c += 1

    return cluster_data, centroids
        

def main():
    filename = './dataset/datasetQ2.csv'
    data = plot_data(filename)

    k = 2

    cluster_arr, centroids = kmeans(data, k)
    print(f"clusters: {cluster_arr}; centroids: {centroids}")

    plot_data(filename, cluster_arr, k, centroids)

main()