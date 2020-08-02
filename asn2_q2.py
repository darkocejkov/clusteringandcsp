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
            csv_reader = reader(obj) #open csv reader object
            line = next(csv_reader) #read line-by-line
            if line != None:
                for row in csv_reader:
                    mpt.plot(float(row[0]), float(row[1]), 'bo') #plot row in float form
                    data.append(row)
        obj.close()  
    else:

        colors = [ #set the color array to support k-means of up to 7 (for clarity)
            'b',
            'r',
            'g',
            'c',
            'y',
            'k',
            'w',
        ]
        
        for x in range(k):
            cluster = arr[x]
            mpt.plot(float(centroid[x][0]), float(centroid[x][1]), colors[x]+"*") #plot centroids in float, as *
            for y in range(len(cluster)):
                mpt.plot(float(cluster[y][0]), float(cluster[y][1]), colors[x]+"o") #plot points as floats, as circles (in their respective cluster color)

    mpt.show()
    mpt.clf()

    return data

def euclid_dist(p1, p2):
    return round(sqrt((float(p1[0]) - float(p2[0]))**2 + (float(p1[1]) - float(p2[1]))**2), 3)
        # calc euclidean distance by sqrt. the squared distance formula
        # round to 3 decimals to encourage convergence
    
def min_index(arr):
    mx = arr[0] #set the minimum value to be the first value
    min_index = 0
    c = 0
    for x in arr:
        if(x < mx): #if current value < min value, then set min value = curr value and grab index c
            mx = x
            min_index = c
        c += 1

    return min_index

def kmeans(data, k):
    centroids = []
    for x in range(k):
        centroids.append(data.pop(0)) #take first k points as centroids (only for first run)

    # print(data)
    # print(f"centroids: {centroids}")
    
    cluster_data = []
    for x in range(k):
        cluster = []
        cluster_data.append(cluster) #make cluster_data a 2D array (array that holds arrays)
            # in this case, cluster_data holds the all the clusters
            # while a "cluster" array holds all the points for a given cluster

    old_centroids = [] #reset the old centroids

    converge = False #flag to stop when centroids converge
    c = 0
    while(not converge):
        print(f"RUN {c+1}")

        idx = 0
        for datum in data: 
            dist = []
            for x in range(k): #calc euclidean dist. from EVERY point to EVERY centroid
                dist.append(euclid_dist(datum, centroids[x]))  #dist holds the distance of a single point to all centroids

            closest_cluster_idx = min_index(dist) #find the closest centroid via function, return index
            local_cluster = cluster_data[closest_cluster_idx] #a cluster is defined by its index
            
            for x in range(k): 
                if(x != closest_cluster_idx):
                    if(datum in cluster_data[x]):
                        cluster_data[x].remove(datum) #if a point is in another cluster, but is now closer to another
                            # remove the point from the other cluster
                else:
                    if(datum not in local_cluster):
                        local_cluster.append(datum) # assign a point to the (possibly new) nearest cluster

            idx += 1

        #once all points have been sorted into their respective cluster, put initial centroids back (only for first run)
        if(c == 0):
            for x in range(k):
                cluster_data[x].append(centroids[x])

        old_centroids = deepcopy(centroids) #create a deepcopy of the current centroids to become old_centroids

        #calculate the new centroids
        for x in range(k):
            local_cluster = cluster_data[x] #all points of a single cluster
            i = 0
            j = 0
            length = len(local_cluster)
            for y in range(length):
                i += int(local_cluster[y][0]) #sum x-values of coord
                j += int(local_cluster[y][1]) #sum y-values of coord

            i = round(i/length, 3) #divide x-sum by how many points there are in the cluster
            j = round(j/length, 3) #divide y-sum by how many points there are in the cluster

            new_centroid = [i,j] #the new centroid is now the (x, y) coord of averaged points
            centroids[x] = new_centroid

        if(centroids == old_centroids):
            converge = True
        else:
            c += 1

    return cluster_data, centroids, c #centroids now contains the last centroids
        

def main():
    filename = './dataset/datasetQ2.csv'
    data = plot_data(filename)

    k = 2 #k-means variable dictating the amount of clusters

    cluster_arr, centroids, c = kmeans(data, k)

    print(f"clusters: {cluster_arr};\n centroids: {centroids}") #report clusters and findings
    print(f"cluster sizes: ")
    for x in range(k):
        print(f"cluster {x+1}: {len(cluster_arr[x])}")
    print(f"runs taken to converge: {c}")

    plot_data(filename, cluster_arr, k, centroids)

main()